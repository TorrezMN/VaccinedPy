"""Collection of Cereal repositories"""
from dagster import repository



#  JOBS
from jobs.vacc_jobs import download_csv_dataset
#  SCHEDULES


@repository
def vacc_repo():
    """Vaccined repository."""
    return [download_csv_dataset]
