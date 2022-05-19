"""Collection of Cereal ops"""
import os
import subprocess
import sys
from datetime import datetime
from os.path import exists
from pathlib import Path
from time import sleep

import pandas as pd
#  DAGSTER
from dagster import (RunRequest, ScheduleDefinition, file_relative_path,
                     get_dagster_logger, graph, job, op, repository, sensor)
#  from dagster_shell import create_shell_command_op, create_shell_script_op
from db_engine.database import SessionLocal
#  IMPORT CRUD OPERATIONS
from db_engine.dose_crud import get_all_dose, get_or_create_new_dose
from db_engine.establishments_crud import get_or_create_establishment
from db_engine.records_crud import (
    filter_record_by_ci, 
    update_record,
    save_new_record)

from db_engine.vaccine_crud import get_or_create_vaccine
#  SCHEMAS
from schemas.dose_schemas import Dose_Name
from schemas.establishments_schemas import Establishments_Name
from schemas.record_chemas import Record
from schemas.vaccine_schemas import Vaccine_Name


BASE_DIR = Path(__file__).resolve().parent.parent


@op
def incert_update_record(chunk):
    """Incert a new record in the database."""

    logger = get_dagster_logger()
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

            logger.warn('A RECORD WAS UPDATED!')

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
    """Read the dataset and process the data in groups of 500 records."""

    logger = get_dagster_logger()
    logger.info('ESTE ES EL READ_CSV OP')
    csv_file_dir = os.path.join(BASE_DIR, 'jobs', 'csv_data', 'covid_py.csv')
    df = pd.read_csv(csv_file_dir, delimiter=';', chunksize=500)
    c = 0
    for k, chunk in enumerate(df):
        if(c<1):
            #  LOAD RECORD
            logger.info(f'LOADING CHUNK - {k}!')
            incert_update_record(chunk)
            c+=1
        else:
            break
