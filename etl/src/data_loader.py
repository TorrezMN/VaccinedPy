import os
import subprocess
import sys
from datetime import datetime
from os.path import exists
from pathlib import Path
from time import sleep

import pandas as pd
#  DAGSTER
from dagster import file_relative_path, get_dagster_logger, job, op
from dagster_shell import create_shell_command_op, create_shell_script_op
from db_engine.database import SessionLocal
#  IMPORT CRUD OPERATIONS
from db_engine.dose_crud import get_all_dose, get_or_create_new_dose
from db_engine.establishments_crud import get_or_create_establishment
from db_engine.records_crud import filter_record_by_ci, save_new_record
from db_engine.vaccine_crud import get_or_create_vaccine
#  SCHEMAS
from schemas.dose_schemas import Dose_Name
from schemas.establishments_schemas import Establishments_Name
from schemas.record_chemas import Record
from schemas.vaccine_schemas import Vaccine_Name

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

main_logger = get_dagster_logger()

@op
def incert_update_record(chunk):
    #  'nombre',
    #  'apellido',
    #  'establecimiento',
    #  'fecha_aplicacion',
    #  'cedula',
    #  'dosis',
    #  'descripcion_vacuna',
    #  'actualizado_al'
    #  -----
    #  date_string = "01-31-2020 14:45:37"
    format_string = "%Y-%m-%d %H:%M:%S"
    #  datetime.strptime(date_string, format_string)
    #  datetime.datetime(2020, 1, 31, 14, 45, 37)

    db = SessionLocal()

    for index, row in chunk.iterrows():
        record = filter_record_by_ci(db, row['cedula'])
        establecimiento = get_or_create_establishment(
            db,
        Establishments_Name(establishments_name= row['establecimiento']),
        )
        dosis = get_or_create_new_dose(
            db,
            Dose_Name(dose_number = int(row['dosis']))
        )
        descripcion_vacuna = get_or_create_vaccine(
            db,
            Vaccine_Name(vaccine_name= row['descripcion_vacuna'])
        )
        if (record):
            print('EXISTE EL RECORD!')
        else:
            r = Record(
                nombre=row['nombre'],
                apellido=row['apellido'], 
                fecha_aplicacion= datetime.strptime(str(row['fecha_aplicacion']), format_string),
                cedula = row['cedula'],
                establishment=establecimiento.id,
                dose=dosis.id,
                vaccine=descripcion_vacuna.id,
                actualizado_al=datetime.strptime(str(row['actualizado_al']), format_string)
            )
            save_new_record(db, r)
            main_logger.info('A new record was saved.')


    #  print('FECHA APLICACION -> ', row['fecha_aplicacion'])
    #  print('ACTUALIZADO AL -> ', row['actualizado_al'])
    db.close()


@op
def read_csv_file():
    csv_file_dir = 'csv_data/covid_py.csv'
    df = pd.read_csv(csv_file_dir, delimiter=';', chunksize=500)
    for k, chunk in enumerate(df):
        #  LOAD RECORD
        main_logger.info(f'LOADING CHUNK - {k}!')
        incert_update_record(chunk)


@job
def download_csv_dataset():
    a = create_shell_script_op(file_relative_path(
        __file__, "shell_scripts/hello_shell.sh"),
                               name="a")
    file_exists = exists(
        os.path.join(BASE_DIR, 'src', 'csv_data', 'covid_py.csv'))

    if (file_exists):
        pass
    else:
        a()

    read_csv_file()
