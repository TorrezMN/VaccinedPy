"""Example of how to run a Dagster op from normal Python script."""
#  from jobs.cereal_jobs import complex_job
from jobs.vacc_jobs import download_csv_dataset

if __name__ == "__main__":
    result = download_csv_dataseg.execute_in_process()
