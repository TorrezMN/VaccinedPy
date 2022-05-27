"""Collection of Cereal jobs"""

import os
from pathlib import Path
from os.path import exists

#  DAGSTER
from dagster import ( file_relative_path,get_dagster_logger, job)
#  OPS
from ops.vacc_ops import download_csv,read_csv_file
    


BASE_DIR = Path(__file__).resolve().parent.parent



@job
def download_csv_dataset():
    """Downaloads a new copy of the dataset if not exists."""
    logger = get_dagster_logger()
    #  file_exists = exists(os.path.join(BASE_DIR, 'csv_data', 'covid_py.csv'))

    download_csv()



    #  if (file_exists):
        #  logger.info('READING CSV FILE!')
        #  read_csv_file()
    #  else:
        #  logger.info('FILE NOT FOUND! - DOWNLOADING NEW COPY')
        #  download_csv()

