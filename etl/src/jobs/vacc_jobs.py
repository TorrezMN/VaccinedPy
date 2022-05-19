"""Collection of Vaccined API jobs"""
import os
from os.path import exists
from pathlib import Path

from dagster import (RunRequest, ScheduleDefinition, file_relative_path,
                     get_dagster_logger, graph, job, op,Nothing, repository, sensor)
from dagster_shell import create_shell_command_op, create_shell_script_op



#  IMPORTING OPS
from ops.transform_ops import read_csv_file

BASE_DIR = Path(__file__).resolve().parent.parent



@job
def download_csv_dataset():
    logger = get_dagster_logger()
    download_dataset = create_shell_script_op(file_relative_path(
        __file__, "shell_scripts/download_csv_file.sh"),
                               name="Download_CSV_Data")

    file_exists = exists(
        os.path.join(BASE_DIR, 'jobs', 'csv_data', 'covid_py.csv'))


    if (file_exists):
        logger.info('FILE EXIST!')
        read_csv_file()
    else:
        logger.info("FILE DON'T EXIST! DOWNLOADING NOW!")
        download_dataset()



