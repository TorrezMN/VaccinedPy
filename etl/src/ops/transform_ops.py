"""Collection of Cereal ops"""
import csv
from typing import List

import requests
from dagster import Nothing, get_dagster_logger, op



@op
def test_op() -> Nothing:
    logger = get_dagster_logger()
    logger.info('ESTE ES UN TEST OP!')


@op
def test_op_2()->Nothing:
    logger = get_dagster_logger()
    logger.info('ESTE ES EL OP 2')

@op 
def test_op_3()->Nothing:
    logger = get_dagster_logger()
    logger.info('ESTE ES EL OP 3')

