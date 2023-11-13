from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import psycopg2
import pandas as pd
from clickhouse_driver import Client
import os
from config import base_dir, python_path, default_args



def get_command(file_nane, commad):
    command = f'{python_path} {base_dir}/Rembo-Project-Assigment/{file_nane} -c {commad}'
    return command

# Define the DAG
dag = DAG(
    'rembo_etl_pg_clickhouse',
    default_args=default_args,
    schedule_interval='10 12 * * *',  # Adjust the schedule as needed
    start_date=datetime(2023, 10, 16),
    catchup=False,
)

generate_fake_data = BashOperator(
    task_id='generate_fake_data',
    bash_command=get_command('main.py', 'generate_fake_data'),
    dag=dag,
)

load_to_postgresql = BashOperator(
    task_id='load_to_postgresql',
    bash_command=get_command('main.py', 'load_to_postgresql'),
    dag=dag,
)

extract_and_load_to_clickhouse = BashOperator(
    task_id='extract_and_load_to_clickhouse',
    bash_command=get_command('main.py', 'extract_and_load_to_clickhouse'),
    dag=dag,
)

generate_fake_data >> load_to_postgresql >> extract_and_load_to_clickhouse
