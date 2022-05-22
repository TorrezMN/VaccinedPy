"""Collection of Cereal repositories"""
from dagster import repository



#  JOBS
from jobs.vacc_jobs import test_job
#  SCHEDULES
from schedules.vacc_schedules import every_weekday_9am 


@repository
def hello_cereal_repository():
    """Vaccined repository."""
    return [test_job, every_weekday_9am]
