"""Collection of Cereal schedules"""

from dagster import schedule

#  JOBS
from jobs.vacc_jobs import test_job


@schedule(
    cron_schedule="*/5 * * * *",
    job=test_job,
    execution_timezone="Europe/Stockholm",
)
def every_five_minutes(context):
    """THIS WILL RUN EVERY FIVE MINUTES."""
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"download_csv": {"config": {"date": date}}}}
