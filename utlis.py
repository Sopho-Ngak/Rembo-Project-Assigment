import time
import psycopg2
import logging
import sys
from random import randint

from clickhouse_driver import Client
import clickhouse_connect
import config as settings
from faker import Faker
import csv
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

def postgres_connection():
    log.info("Connecting to postgres")
    engine = create_engine(f'postgresql+psycopg2://{settings.pg_user}:{settings.pg_password}@{settings.pg_host}:{settings.pg_port}/{settings.pg_dbname}')
    conn = engine.connect()
    log.info("Connection to postgres established")
    return conn

def clickhouse_connection():
    log.info("Connecting to clickhouse")
    conn = clickhouse_connect.get_client(
        host=settings.clickhouse_host, 
        port=settings.clickhouse_port, 
        user=settings.clickhouse_user, 
        password=settings.clickhouse_password,
        database=settings.clickhouse_db
        )
    log.info(f"Connection to clickhouse established: { conn.query_df('SHOW TABLES FROM rembo_olap')}")
    return conn

'''
CREATE TABLE Sales(
Sales_Id SERIAL NOT NULL,
CurrencyKey varchar(50) NULL,
CustomerKey varchar(50) NULL,
Discount_Amount varchar(50) NULL,
DueDate varchar(50) NULL,
DueDateKey varchar(50) NULL,
Extended_Amount varchar(50) NULL,
Freight varchar(50) NULL,
Order_Date varchar(50) NULL,
Order_Quantity varchar(50) NULL,
Product_Standard_Cost varchar(50) NULL,
Revision_Number varchar(50) NULL,
Sales_Amount varchar(50) NULL,
Sales_Order_Line_Number varchar(50) NULL,
Sales_Order_Number varchar(50) NULL,
SalesTerritoryKey varchar(50) NULL,
ShipDate varchar(50) NULL,
Tax_Amt varchar(50) NULL,
Total_Product_Cost varchar(50) NULL,
Unit_Price varchar(50) NULL,
Unit_Price_Discount_Pct varchar(50) NULL,
Employee_Id INT NOT NULL,
PRIMARY KEY (Sales_Id),
FOREIGN KEY (Employee_Id) REFERENCES Employee (Employee_Id)
FOREIGN KEY (Sales_Territory_Id) REFERENCES Sales_Territory (Sales_Territory_Id)
)

'''

# def get_colums(tabel_name):
columns = {
    'Customer':[
        'Customer_Id',
        'Last_Name',
        'Address_line1',
        'Address_line2',
        'Birth_Date',
        'Age',
        'Commute_Distance',
        'Customer_Alternate_Key',
        'Customer_Key',
        'Date_First_Purchase',
        'Email_Address',
        'English_Education',
        'English_Occupation',
        'French_Education',
        'First_Name',
        'Gender',
        'House_Owner_Flag',
        'Marital_Status',
        'Middle_Name',
        'Name_Style',
        'Number_Cars_Owned',
        'Number_Children_At_Home',
        'Phone',
        'Spanish_Education',
        'Spanish_Occupation',
        'Suffix',
        'Title',
        'Total_Children',
        'Yearly_Income'
        ],
    'Sales_Territory':[
        'Sales_Territory_Id',
        'Sales_Territory_Country',
        'Sales_Territory_Region',
        'Sales_Territory_City'
        ],
    'Employee':[
        'Employee_Id',
        'Employee_Name',
        'Employee_Territory_Region'
        ],
    'Sales':[
        'Sales_Id',
        'CurrencyKey',
        'CustomerKey',
        'Discount_Amount',
        'DueDate',
        'DueDateKey',
        'Extended_Amount',
        'Freight',
        'Order_Date',
        'Order_Quantity',
        'Product_Standard_Cost',
        'Revision_Number',
        'Sales_Amount',
        'Sales_Order_Line_Number',
        'Sales_Order_Number',
        'SalesTerritoryKey',
        'ShipDate',
        'Tax_Amt',
        'Total_Product_Cost',
        'Unit_Price',
        'Unit_Price_Discount_Pct',
        'Employee_Id',
        'Customer_Id',
        'Sales_Territory_Id',
        ]
}

    # return columns[tabel_name]


def generate_csv_files_with_data():
    fake = Faker()
    
    with open(f'{settings.base_dir}/Rembo-Project-Assigment/csv/customer.csv', 'w') as customer:
        log.info("Generating fake data for customers")
        writer = csv.writer(customer)
        writer.writerow(columns['Customer'])
        for n in range(1, 1001):
            writer.writerow([
                randint(1, 1000),
                fake.last_name(),
                fake.address(),
                fake.address(),
                fake.date(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.date(),
                fake.email(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.first_name(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.phone_number(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int()
            ])

    log.info("Generating fake data for sales_territory")
    with open(f'{settings.base_dir}/Rembo-Project-Assigment/csv/sales_territory.csv', 'w') as sales_territory:
        writer = csv.writer(sales_territory)
        writer.writerow(columns['Sales_Territory'])
        for n in range(1, 8):
            writer.writerow([
                randint(1, 1000),
                fake.country(),
                fake.city(),
                fake.city()
            ])

    log.info("Generating fake data for employee")
    with open(f'{settings.base_dir}/Rembo-Project-Assigment/csv/employee.csv', 'w') as employee:
        writer = csv.writer(employee)
        writer.writerow(columns['Employee'])
        for n in range(1, 1001):
            writer.writerow([
                randint(1, 1000),
                fake.name(),
                fake.city()
            ])

    log.info("Generating fake data for sales")
    with open(f'{settings.base_dir}/Rembo-Project-Assigment/csv/sales.csv', 'w') as sales:

        writer = csv.writer(sales)
        writer.writerow(columns['Sales'])
        for n in range(1, 100):
            writer.writerow([
                randint(1, 1000),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.date(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.date(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.date(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                fake.random_int(),
                randint(1, 1000),
                randint(1, 1000),
                randint(1, 1000)
            ])
    



def load_to_postgresql():
    conn = postgres_connection()
    # cur = conn.cursor()
    for table in columns:
        log.info(f"Loading data to postgres table: {table}")
        df = pd.read_csv(f'{settings.base_dir}/Rembo-Project-Assigment/csv/{table.lower()}.csv')
        log.info(f"Data loaded to pandas dataframe")
        df.to_sql(table.lower(), conn, if_exists='append', index=False)
        log.info(f"Data loaded to postgres table: {table}")
