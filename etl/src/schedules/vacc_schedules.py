"""Collection of Cereal schedules"""

from dagster import schedule

#  JOBS
from jobs.vacc_jobs import test_job


@schedule(
    cron_schedule="*/5 * * * *",
    job=test_job,
    execution_timezone="Europe/Stockholm",
)
def every_weekday_9am(context):
    """Example of how to setup a weekday schedule for a job."""
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"test_op": {"config": {"date": date}}}}
