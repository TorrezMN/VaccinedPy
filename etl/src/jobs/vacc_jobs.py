"""Collection of Cereal jobs"""
from dagster import job

from ops.vacc_ops import test_op  





@job
def test_job():
    """Este es un trabajo de prueba."""
    test_op()
