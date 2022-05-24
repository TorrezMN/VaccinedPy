"""Collection of Cereal repositories"""
from dagster import repository



#  JOBS
from jobs.vacc_jobs import test_job
#  SCHEDULES
from schedules.vacc_schedules import every_five_minutes 


@repository
def vacc_repo():
    """Vaccined repository."""
    return [test_job, every_five_minutes]
