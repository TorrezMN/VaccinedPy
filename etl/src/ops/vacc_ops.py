"""Collection of Cereal ops"""
import csv
import requests
from time import sleep
from typing import List
from dagster import Nothing, get_dagster_logger, op



@op
def download_csv() -> Nothing:
    """Este es un op de prueba."""
    logger = get_dagster_logger()
    for i in range(0,10):
        sleep(5)
        logger.info("ESTE ES EL DOWNLOAD CSV!")
    read_csv()
@op
def read_csv() -> Nothing:
    """Este es un op de prueba."""
    logger = get_dagster_logger()
    for i in range(0,10):
        sleep(2)
        logger.info("ESTE ES EL READ_CSV!")
        save_update_record()
    
@op
def save_update_record() -> Nothing:
    """Este es un op de prueba."""
    logger = get_dagster_logger()
    for i in range(0,10):
        logger.info("ESTE ES EL SAVE UPDATE RECORD!")
