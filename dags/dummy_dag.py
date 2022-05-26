from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "description": "Example DAG",
    "start_date": datetime(2022, 5, 25),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "concurrency": 1,
    "depends_on_past": False,
    "max_active_runs_per_dag": 1,
}


def dummy_function(variable1):
    print(f"This is the value of variable1: {variable1}")
    # you could do something else here
    return None  # returned values can be passed to other downstream tasks


with DAG(
    "dummy_example",  # this name needs to be unique across all DAGs
    default_args=default_args,
    catchup=False,
    schedule_interval="@daily",  # this can be set to daily, weekly, monthly or cron
) as dag:
    dummy_task1 = DummyOperator(
        task_id="dummy_task_1"  # all tasks names need to be unique inside the same DAG, and are a must for each task
    )

    dummy_task2 = DummyOperator(task_id="dummy_task_2")

    # there are different kind of operators, normally you would use BashOperators, PythonOperators and DockerOperators
    dummy_function = PythonOperator(
        task_id="dummy_function",
        python_callable=dummy_function,
        op_args=[
            "hey",
        ],
    )

    dummy_task1 >> dummy_task2
    dummy_task1 >> dummy_function
