To address the business challenges outlined for Sales and Operations, we'll design a system that involves data extraction, transformation, loading (ETL), and real-time reporting using PostgreSQL as the source OLTP database and ClickHouse as the destination OLAP database. We'll also create a sample data pipeline and dashboard for a practical demonstration.

First, we need to create tables in ClickHouse that match the schema in PostgreSQL and generate sample data.
The clickhouse queries to create the necesseries table are in this file: Rembo-Project-Assigment/Queries/clickhouse_queries.sql

Data Modeling:

We need to model the data and establish relationships between tables as specified in the given PostgreSQL schema. Each table will be imported into ClickHouse, and we will create an OLAP schema that mirrors the OLTP structure. However, we might denormalize some data for performance optimization.
We added two addional field in sales table
    1. Customer_Id: To link the to the customer table (Foreign Key)
    2. Sales_Territory_Id: To link to the Sales_Territory table to know where the sale has been made (Foreign Key)

Sales Table in ClickHouse:

    We'll model this table with ClickHouse data types and possibly use nested structures to store more complex data.
    We may add a materialized view to calculate additional metrics (e.g., sales by employee, top customers, YoY change) to speed up queries.

Data Population:

We need to populate the ClickHouse database with data from PostgreSQL. This can be achieved using ETL (Extract, Transform, Load) processes. For this I propose to use python script for the ETL, and airflow to perform real-time data ingestion pipeline. Data can be streamed from PostgreSQL to ClickHouse.
To achieve real-time data processing within 20 seconds, we can schedule our Airflow DAG to run at regular intervals (e.g., every minute or every 5 min). This will allows to get close to real-time data updates.



Data Extraction:

We'll use the sqlalchemy library to connect to the PostgreSQL database and extract data from the Sales and Employee tables. We'll then transform the data and load it into the ClickHouse database.
But before doing that as for this example we need to populate the PostgreSQL database with some sample data. We'll use the Faker library to generate sample data for the Sales,Employee, customer tables. This will runing in the airflow dag.

Handling Data Processing Failures:

Airflow provides built-in mechanisms for handling task retries and notifications on failure. We can configure it to retry failed tasks or notify responsible personnel in case of a failure. This will help to ensure that data is processed in a timely manner and that the system is working properly.

Data Transformation:

We'll transform the data to calculate sales metrics, employee performance, and customer insights. We'll also create a materialized view to speed up queries. But for this exemple I prefer to use Power BI to connect to clickhouse and run the query for transformation for dashboard repport.

System Design Flow:

    Data Extraction: Data will be extracted in real-time from the PostgreSQL database, mainly from the Sales and Employee tables.

    Data Transformation: Real-time data will be transformed to calculate sales metrics, employee performance, and customer insights.

    Data Loading: Transformed data will be loaded into the ClickHouse OLAP database.

    Real-time Reporting: A real-time dashboard will be built to provide insights into sales and organizational metrics.



ClickHouse Dashboard and Power BI Reports

We can connect Power BI to ClickHouse as a data source using the ODBC driver for ClickHouse. Create the necessary reports and dashboards in Power BI to address the specific business challenges mentioned in the context.

For example, to address the Sales challenges:

    Create a report showing top employees by product sales.
    Create a report showing the top 100 customers for each territory with metrics like the average time between purchases and the average purchase price.

To address the Operations challenges:

    Create a report showing the year-over-year change in sales across the organization.
    Create a real-time view of sales by region and country.


Step To Follo To Create Power BI Repport Dashbord
    Most Important Step:
        Download and install the ODBC driver for ClickHouse.
        Create a DSN for ClickHouse.
        Connect Power BI to ClickHouse using the DSN.
        Create the necessary reports and dashboards in Power BI.

To create reports in Power BI that address the challenge of showing top employees by product sales and the top 100 customers for each territory with metrics, we can follow these steps:

1. Import Data:

Import our data from ClickHouse into Power BI. We can use the ODBC driver for ClickHouse to connect to our ClickHouse database.

2. Create a Report for Top Employees by Product Sales:

To create a report showing top employees by product sales, We can follow these steps:

    a. Create a new page in Power BI report.

    b. Add a table or matrix visual.

    c. Drag the "Employee Name" field to the Rows section.

    d. Drag the "Sales Amount" field to the Values section.

    e. Sort the table or matrix by "Sales Amount" in descending order.

    f. Limit the table to display only the top N employees (e.g., top 10) by going to the "Visualizations" pane, expanding "Filters," and setting a filter based on the "Rank" or "Sales Amount."


3. Create a Report for Top 100 Customers by Territory:

To create a report showing the top 100 customers for each territory with metrics like the average time between purchases and the average purchase price, We can follow these steps:

    a. Create a another page in Power BI report.

    b. Add a table or matrix visual.

    c. Drag the "Sales Territory" field to the Rows section.

    d. Drag the "Customer Name" field to the Values section.

    e. Sort the table or matrix by "Customer Name" in descending order.

    f. Limit the table to display only the top 100 customers for each territory by going to the "Visualizations" pane, expanding "Filters," and setting a filter based on the "Rank" or "Customer Name."

    g. To calculate metrics like the average time between purchases and the average purchase price, we can create new measures in Power BI. Here's an example of DAX measures we can create:

    Average Time Between Purchases:

    Average Time Between Purchases = 
        AVERAGEX(
            FILTER(
                ALL('Sales'),
                'Sales'[Customer Name] = SELECTEDVALUE('Sales'[Customer Name])
            ),
            DATEDIFF(
                EARLIER('Sales'[Order Date]),
                'Sales'[Order Date],
                DAY
            )
        )

    Average Purchase Price:

        Average Purchase Price = 
        AVERAGE('Sales'[Sales Amount])

    We can add these measures to our table or matrix visual to display the metrics for the top 100 customers in each territory.

Publish and Share the Report:

Once we've created the necessary reports and dashboards in Power BI, we can publish them to Power BI Service and share them with our colleagues. We can also embed the reports in our website or application using the Power BI JavaScript API.

