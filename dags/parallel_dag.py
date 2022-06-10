from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import json
from pandas import json_normalize

default_args = {"start_date": datetime(2020, 1, 1)}

with DAG(
    "parallel_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:
    task_1 = BashOperator(task_id='task_1', bash_command='sleep 3')
    task_2 = BashOperator(task_id='task_2', bash_command='sleep 3')
    task_3 = BashOperator(task_id='task_3', bash_command='sleep 3')
    task_4 = BashOperator(task_id='task_4', bash_command='sleep 3')


    task_1 >> [task_2, task_3] >> task_4
