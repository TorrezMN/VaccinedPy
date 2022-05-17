"""Collection of Vaccined API jobs"""
import os
from os.path import exists
from pathlib import Path


from dagster import (RunRequest, ScheduleDefinition, file_relative_path,
                     get_dagster_logger, graph, job, op, repository, sensor)
from dagster_shell import create_shell_command_op, create_shell_script_op

from ops.cereal_ops import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)



BASE_DIR = Path(__file__).resolve().parent.parent



@job
def download_csv_dataset():
    a = create_shell_script_op(file_relative_path(
        __file__, "shell_scripts/download_csv_file.sh"),
                               name="a")


    file_exists = exists(
        os.path.join(BASE_DIR, 'src', 'csv_data', 'covid_py.csv'))

    if (file_exists):
        pass
    else:
        a()

    # After downloading csv data. Process data.
    #  read_csv_file()


