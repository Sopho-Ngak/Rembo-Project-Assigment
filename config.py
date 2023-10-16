# import load env
import sys
import os
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

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
