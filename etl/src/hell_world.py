import os
import subprocess
from os.path import exists
from pathlib import Path
from time import sleep

import pandas as pd
from dagster import file_relative_path, graph, job, op, pipeline
from dagster_shell import create_shell_command_op, create_shell_script_op

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


@op
def print_row(row):
    print('ROW ----------> ', row)

@op
def read_csv_file():
    csv_file_dir = 'csv_data/covid_py.csv'
    df = pd.read_csv(csv_file_dir, delimiter=';', chunksize=100)
    print('==============================================')
    print('BASE DIR FROM READ_CSV FILE!', BASE_DIR)
    print('==============================================')
    for chunk in df:
        chunk.apply(print_row)
    print('==============================================')




@graph
def download_csv_dataset():
    a = create_shell_script_op(file_relative_path(__file__, "shell_scripts/hello_shell.sh"), name="a")
    file_exists = exists(os.path.join(BASE_DIR, 'src', 'csv_data', 'covid_py.csv'))


    if(file_exists):
        print('YA SE DESCARGO EL ARCHIVO!')
    else:
        a()


    print('==============================================')
    read_csv_file()
    print('==============================================')






@op
def get_name():
    sleep(3)
    return "dagster"


@op
def hello(name: str):
    sleep(5)
    print(f"Hello, {name}!")


@job
def hello_dagster():
    sleep(10)
    hello(get_name())
    download_csv_dataset()
