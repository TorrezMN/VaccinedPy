#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import os
from decouple import config

from data_loader import load_dataset


def download_data():
    FILE_PATH = 'api/db_engine/helper_scripts/vacunados.csv'

    if (os.path.exists(FILE_PATH)):
        print('EL ARCHIVO EXISTE')
    else:
        print('GETTING DATA')
        os.system('sh api/db_engine/helper_scripts/download_data.sh')


if __name__ == '__main__':
    download_data()
    load_dataset()
