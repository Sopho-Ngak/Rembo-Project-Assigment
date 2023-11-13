# import load env
import sys
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
python_path = os.path.join(base_dir, 'Rembo-Project-Assigment/env/bin/python3.10')

pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_host = os.getenv("PG_HOST")
pg_port = os.getenv("PG_PORT")
pg_dbname = os.getenv("PG_DATABASE")

clickhouse_user = os.getenv("CLICKHOUSE_USER")
clickhouse_password = os.getenv("CLICKHOUSE_PASSWORD")
clickhouse_host = os.getenv("CLICKHOUSE_HOST")
clickhouse_port = os.getenv("CLICKHOUSE_PORT")
clickhouse_db = os.getenv("CLICKHOUSE_DB")
clickhouse_interface = os.getenv("CLICKHOUSE_INTERFACE")

default_args = {
    'owner': 'rembo',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 16),
    'email': ['sopho.ngak@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}
