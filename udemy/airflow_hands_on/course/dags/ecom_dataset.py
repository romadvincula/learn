from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from pendulum import datetime, duration
from include.datasets import DATASET_COCKTAIL


@dag(start_date=datetime(2025, 11, 1, tz="Australia/Sydney"),
     schedule=[DATASET_COCKTAIL],
     catchup=False,
     description="This DAG processes ecommerce data",
     tags=["team_a", "ecom"],
     default_args={"retries": 2},
     dagrun_timeout=duration(minutes=20),
     max_consecutive_failed_dag_runs=2
     )
def ecom_dataset():

    ta = EmptyOperator(task_id='ta')


ecom_dataset()