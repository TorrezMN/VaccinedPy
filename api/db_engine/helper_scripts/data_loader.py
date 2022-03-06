#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import os
import pandas as pd

df = None

#  DATAFRAME FIELDS
#  ==========================
#  'nombre'
#  'apellido'
#  'establecimiento'
#  'fecha_aplicacion'
#  'cedula'
#  'dosis'
#  'descripcion_vacuna'
#  'actualizado_al'


def analize_chunck(chunk):
    keys = chunk['descripcion_vacuna'].value_counts(normalize=True).keys()
    print(keys)


def load_dataset():
    FILE_LOC = 'api/db_engine/helper_scripts/vacunados.csv'
    df = pd.read_csv(FILE_LOC, delimiter=';', chunksize=500)
    for i in df:
        analize_chunck(i)
