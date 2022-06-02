"""Collection of Cereal ops"""
import csv
import requests
from time import sleep
from typing import List
import os
import subprocess
import ssl
import wget
import sys
import pandas as pd
from datetime import datetime
from time import sleep

from decouple import config

#  DAGSTER
from dagster import (get_dagster_logger, op)

#  DB
from db_engine.database import SessionLocal
#  IMPORT CRUD OPERATIONS
from db_engine.dose_crud import get_all_dose, get_or_create_new_dose
from db_engine.establishments_crud import get_or_create_establishment
from db_engine.records_crud import (filter_record_by_ci, save_new_record)
from db_engine.vaccine_crud import get_or_create_vaccine
#  SCHEMAS
from schemas.dose_schemas import Dose_Name
from schemas.establishments_schemas import Establishments_Name
from schemas.record_chemas import Record
from schemas.vaccine_schemas import Vaccine_Name


@op
def download_csv():
    logger = get_dagster_logger()
    logger.info("DOWNLOADING CSV FILE!")
    ssl._create_default_https_context = ssl._create_unverified_context
    #  DOWNLOADING FILE
    wget.download(config('BASE_URL', cast=str), out='csv_data/covid_py.csv')
    read_csv_file()
        

@op
def incert_update_record(chunk):
    logger = get_dagster_logger()
    logger.info('INCERTING A NEW RECORD!')
    format_string = "%Y-%m-%d %H:%M:%S"
    db = SessionLocal()
    for index, row in chunk.iterrows():
        record = filter_record_by_ci(db, row['cedula'])
        if (record):
            r = Record(
            nombre=row['nombre'],
            apellido=row['apellido'],
            fecha_aplicacion= datetime.strptime(str(row['fecha_aplicacion']), format_string),
            cedula = row['cedula'],
            establishment=get_or_create_establishment(
            db,
            Establishments_Name(establishments_name= row['establecimiento']),
            ).id,
            dose=get_or_create_new_dose(
            db,
            Dose_Name(dose_number = int(row['dosis']))
            ).id,
            vaccine=get_or_create_vaccine(
            db,
            Vaccine_Name(vaccine_name= row['descripcion_vacuna'])
            ).id,
            actualizado_al=datetime.strptime(str(row['actualizado_al']), format_string)
            )
            update_record(db, row['cedula'], r)

            logger.info('A RECORD WAS UPDATED!')

        else:
            r = Record(
            nombre=row['nombre'],
            apellido=row['apellido'],
            fecha_aplicacion= datetime.strptime(str(row['fecha_aplicacion']), format_string),
            cedula = row['cedula'],
            establishment=get_or_create_establishment(
            db,
            Establishments_Name(establishments_name= row['establecimiento']),
            ).id,
            dose=get_or_create_new_dose(
            db,
            Dose_Name(dose_number = int(row['dosis']))
            ).id,
            vaccine=get_or_create_vaccine(
            db,
            Vaccine_Name(vaccine_name= row['descripcion_vacuna'])
            ).id,
            actualizado_al=datetime.strptime(str(row['actualizado_al']), format_string)
            )
            save_new_record(db, r)
            logger.info('A NEW RECORD WAS SAVED!')
    db.close()



@op
def read_csv_file():
    logger = get_dagster_logger()
    logger.info('READING CSV FILE!')
    csv_file_dir = 'csv_data/covid_py.csv'
    df = pd.read_csv(csv_file_dir, delimiter=';', chunksize=500)
    limit = config('LOAD_CHUNKS', cast=int)
    c = 0
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f'DOWNLOADING config set to: {c}')
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    logger.info(f"ES INSTANCIA {isinstance(c, int)}")
    if(isinstance(c, int)):
        logger.info('LOAD_CHUNKS was found in config.')
        for k, chunk in enumerate(df):
            if(c<limit):
                #  LOAD RECORD
                logger.info(f'LOADING CHUNK - {k}!')
                incert_update_record(chunk)
                c+=1
            else:
                break
        remove_csv_file()
    else:
        logger.info('LOAD_CHUNKS was not found in config.')
        for k, chunk in enumerate(df):
            #  LOAD RECORD
            logger.info(f'LOADING CHUNK - {k}!')
            incert_update_record(chunk)

        remove_csv_file()

@op
def remove_csv_file():
    logger = get_dagster_logger()
    csv_file_dir = 'csv_data/covid_py.csv'
    logger.info('REMOVING CSV FILE!')
    try:
        os.remove(csv_file_dir)
        logger.info('FILE WAS REMOVED SUCCESFULY!')
    except:
        logger.info('IT WAS NOT POSIBLE TO DELETE THE CSV FILE!')




