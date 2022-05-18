"""Collection of Vaccined API jobs"""
import os
from os.path import exists
from pathlib import Path


from dagster import (RunRequest, ScheduleDefinition, file_relative_path,
                     get_dagster_logger, graph, job, op, repository, sensor)
from dagster_shell import create_shell_command_op, create_shell_script_op



from ops.transform_ops import test_op

BASE_DIR = Path(__file__).resolve().parent.parent



@job
def download_csv_dataset():
    download_dataset = create_shell_script_op(file_relative_path(
        __file__, "shell_scripts/download_csv_file.sh"),
                               name="a")


    file_exists = exists(
        os.path.join(BASE_DIR, 'src', 'csv_data', 'covid_py.csv'))

    if (file_exists):
        pass
    else:
        download_dataset()

    test_op()
    # After downloading csv data. Process data.


