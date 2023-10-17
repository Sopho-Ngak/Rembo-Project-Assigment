Context
======================================================
Company Rembo sells multiple products in 11 different regions. All regions generate a large amount of data crucial for executive decision-making and measuring business performance. Business teams in the company need data, reports, and insight from the customer management system to make reports, make informed decisions, and measure business performance daily, weekly, and monthly basis with a particular need from Senior Management of real-time reporting.

The sales teams based at the HQ have a challenge in analyzing the increasingly large amount of data from all territories stored in a centralized database of the company's customer management system (CRM).

There are eleven sales teams in charge of data of each territory, and each sales team wants to manage their own sales data. The Rembo operations team also wants to understand what sales are occurring and where.

Database schema:
    Rembo Company Database Structure has four tables (customer, sales_territory, employee and sales tables) with data recorded at a particular point in time. Below is the link to the gist (public):
    https://bit.ly/3HttVL8(https://gist.github.com/ellykadenyo/18ccdaa2305f3c29accc542b502f7710)

Model your database accordingly with the required table relationships. Populate the database with sample data. If you can, as part of your solution provide a simulator that generates the records in realtime. As a base you should have around 500k records across the customer and sales tables, and 11 records in the sales_territory table.

Assignment:

Sales:
    The Rembo organization wants each team to understand when sales are happening in real
    time.
    1. Each team/territory wants to understand which employees are selling the most products
    2. Each team / territory wants to understand their top 100 customers ( the average time between purchases and the average purchase price).
    3. The latency through the system should accrue to no more than 20 seconds

    4. It should be clear how the system will handle failures in data processing and or system failure.
    Operations:
        The operations team is interested in understanding organizational metrics
        1. The operations team wants to be able to know the Year over Year change of sales across the entire organization.
        2. They want to have a real time view of their sales, by region and country. .

        Instructions:
            1. Using the SQL DDL attached (for PostgreSQL) to this assignment, simulate a data pipeline injection from SQL source to an OLAP destination. (Required: PostgreSQL as a source; Clickhouse as the destination).
            2. Your answer should be precise and directly respond to the business challenges.
            3. Your solution should provide insight into how it would work in production, and a simple working example of the system.

Expected Outcome:
    1. A system design flow which captures the tools, processes and key actors in those processes.
    2. A complete end to end system that includes:
        ● Source OLTP database (PostgreSQL)
        ● Destination OLAP database (Clickhouse)
        ● Data pipeline moving data from source to destination in
        real-time
        ● Dashboard with real-time reports
    3. A practical demo of how the system will work.