"""Collection of Cereal repositories"""
from dagster import repository



#  JOBS
from jobs.vacc_jobs import download_csv_dataset
#  SCHEDULES
from schedules.vacc_schedules import every_five_minutes


@repository
def vacc_repo():
    """Vaccined repository."""
    return [download_csv_dataset, every_five_minutes]
