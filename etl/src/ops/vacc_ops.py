"""Collection of Cereal ops"""
import csv
import requests
from time import sleep
from typing import List
from dagster import Nothing, get_dagster_logger, op



@op
def test_op() -> Nothing:
    """Este es un op de prueba."""
    logger = get_dagster_logger()
    for i in range(0,10):
        sleep(5)
        logger.info("ESTE ES EL OP!")
