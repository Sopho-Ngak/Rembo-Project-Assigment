from datetime import datetime
import logging
import sys
import argparse
from utlis import postgres_connection, clickhouse_connection
from clickhouse_connect.driver.tools import insert_file
import pandas as pd
from utlis import generate_csv_files_with_data, load_to_postgresql, columns as tables
import config as settings

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

TODAY = datetime.today().strftime('%Y-%m-%d')

class DataTransfer:
    def __init__(self):
        self.pg_conn = postgres_connection()
        self.ch_conn = clickhouse_connection()
        self.pg_cursor = self.pg_conn.connection.cursor()
        self.csv_folder = f'{settings.base_dir}/Rembo-Project-Assigment/csv/'

    def get_data_from_pg_src(self, table_name):
        log.info(f"Getting data from postgres table: {table_name}")
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", self.pg_conn)
        df.to_csv(f'{self.csv_folder}{table_name}_{TODAY}.csv', index=False)
        log.info(f"Data from postgres table: {table_name} saved to file: {self.csv_folder}{table_name}_{TODAY}.csv")
        return df

    def insert_data_to_ch(self, data):
        pass

    def insert_data_to_ch_from_file(self):

        for table in tables:

            file_path = f'{self.csv_folder}{table}_{TODAY}.csv'
            self.get_data_from_pg_src(table_name=table)

            log.info(f"Inserting data from file: {file_path} to clickhouse table: {table}")
            insert_file(self.ch_conn, table=table, file_path=file_path, database=settings.clickhouse_db,
                        settings={'input_format_allow_errors_ratio': .2,
                                'input_format_allow_errors_num': 5})
            log.info(f"Data from file: {file_path} inserted to clickhouse table: {table}")
            
        self.close_connections()

    def close_connections(self):
        self.pg_cursor.close()
        self.pg_conn.close()
        self.ch_conn.close()
        self.ch_conn.close()


LIST_COMMANDS = [
    "generate_fake_data",
    "load_to_postgresql", 
    "extract_and_load_to_clickhouse",
    ]

def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    description='ETL for Rembo Project: Load from source OLAP postgresql to clickhouse')

    parser.add_argument("-c","--command_name", type=str, choices = LIST_COMMANDS,  help="Name of the command to be executed", )
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_arguments()
    command_name = args.command_name

    if command_name == "generate_fake_data":
        generate_csv_files_with_data()

    elif command_name == "load_to_postgresql":
        load_to_postgresql()

    elif command_name == "extract_and_load_to_clickhouse":
        DataTransfer().insert_data_to_ch_from_file()
    else:
        log.error(f"Command: {command_name} not found")
        log.info(f"List of available commands: {LIST_COMMANDS}")


    