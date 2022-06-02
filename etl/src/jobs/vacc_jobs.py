"""Collection of Cereal jobs"""

import os
from pathlib import Path
from os.path import exists

#  DAGSTER
from dagster import ( file_relative_path,get_dagster_logger, job)
#  OPS
from ops.vacc_ops import download_csv,read_csv_file
    

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent



@job
def download_csv_dataset():
    """Downaloads a new copy of the dataset if not exists."""
    logger = get_dagster_logger()

    c = config('LOAD_CHUNKS', cast=int)

    download_csv()


