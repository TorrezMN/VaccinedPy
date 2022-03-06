#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import json

import pandas as pd
import requests

ESTABLISHMENT_BASE_URL = 'http://localhost:8000/establishments/get_or_create_establishment'
DOSE_BASE_URL = 'http://localhost:8000/dose/get_or_create_dose'
VACCINE_BASE_URL = 'http://localhost:8000/vaccine/get_or_create_vaccine'

headers = {'content-type': 'application/json'}

#  'nombre'
#  'apellido'
#  'establecimiento'
#  'fecha_aplicacion'
#  'cedula'
#  'dosis'
#  'descripcion_vacuna'
#  'actualizado_al'


def load_establishments(chunk):
    for i in chunk.establecimiento.value_counts().keys():
        data = {"establishments_name": i}
        x = requests.post(ESTABLISHMENT_BASE_URL,
                          data=json.dumps(data),
                          headers=headers)
        print(x.text)


def load_dose(chunk):
    for i in chunk.dosis.value_counts().keys():
        data = {"dose_number": str(i)}
        x = requests.post(DOSE_BASE_URL,
                          data=json.dumps(data),
                          headers=headers)
        print(x.text)


def load_vaccine(chunk):
    for i in chunk.descripcion_vacuna.value_counts().keys():
        data = {"vaccine_name": i}
        x = requests.post(VACCINE_BASE_URL,
                          data=json.dumps(data),
                          headers=headers)
        print(x.text)


def update_models_data():
    FILE_LOC = 'db_engine/helper_scripts/vacunados.csv'
    df = pd.read_csv(FILE_LOC, delimiter=';', chunksize=500)
    for i in df:
        load_establishments(i)
        load_dose(i)
        load_vaccine(i)


def update_records():
    print('Updating records.')
