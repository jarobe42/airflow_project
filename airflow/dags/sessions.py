import logging

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

from airflow.operators.python_operator import PythonOperator

from launcher.launcher import ContainerLauncher
from launcher.docker import do_test_docker

args = {
    'owner': 'airflow',
    'start_date': '2019-01-01'
}


with DAG(dag_id='session_dag', default_args=args, schedule_interval='0 0 * * *') as dag:
    query = """
        INSERT INTO session_aggregation()
    
    """
