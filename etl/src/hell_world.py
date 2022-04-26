from time import sleep

from dagster import job, op


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
