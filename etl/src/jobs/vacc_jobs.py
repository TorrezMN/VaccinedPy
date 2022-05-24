"""Collection of Cereal jobs"""
from dagster import job

from ops.vacc_ops import download_csv  





@job
def test_job():
    """Este es un trabajo de prueba."""
    download_csv()
