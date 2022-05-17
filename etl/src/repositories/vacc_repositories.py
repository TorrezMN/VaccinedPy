"""Collection of Cereal repositories"""
from dagster import repository
from dagster import (RunRequest, ScheduleDefinition, file_relative_path,
                     get_dagster_logger, graph, job, op, repository, sensor)

from jobs.cereal_jobs import complex_job, hello_cereal_job
from jobs.vacc_jobs import download_csv_dataset
from schedules.cereal_schedules import every_weekday_9am


@repository
def vaccined_covid_py_repo():
    """Collection of covid etl jobs."""
    return[download_csv_dataset]

@repository
def hello_cereal_repository():
    """Collection of cereal jobs and other definitions used by Dagster."""
    return [complex_job, hello_cereal_job, every_weekday_9am]
