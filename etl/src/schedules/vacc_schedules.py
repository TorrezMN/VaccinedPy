"""Collection of Cereal schedules"""

from dagster import schedule

from ops.vacc_ops import download_csv
#  JOBS
from jobs.vacc_jobs import download_csv_dataset


@schedule(
    cron_schedule="0 * * * *",
    job=download_csv_dataset,
    execution_timezone="America/Asuncion",
)
def every_five_minutes(context):
    """THIS WILL RUN EVERY FIVE MINUTES."""
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"download_csv": {"config": {"date": date}}}}
