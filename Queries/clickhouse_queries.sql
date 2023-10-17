-- Create a ClickHouse database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS rembo_olap;

-- Create the Customer table
CREATE TABLE IF NOT EXISTS rembo_olap.Customer
(
    Customer_Id UInt32,
    Last_Name String,
    Address_Line1 String,
    Address_Line2 String,
    Birth_Date String,
    Age String,
    Commute_Distance String,
    Customer_Alternate_Key String,
    Customer_Key String,
    Date_First_Purchase String,
    Email_Address String,
    English_Education String,
    English_Occupation String,
    French_Education String,
    First_Name String,
    French_Occupation String,
    Gender String,
    House_Owner_Flag String,
    Marital_Status String,
    Middle_Name String,
    Name_Style String,
    Number_Cars_Owned String,
    Number_Children_At_Home String,
    Phone String,
    Spanish_Education String,
    Spanish_Occupation String,
    Suffix String,
    Title String,
    Total_Children String,
    Yearly_Income String
)
ENGINE = ReplacingMergeTree
PRIMARY KEY (Customer_Id)

-- Create the Sales_Territory table
CREATE TABLE IF NOT EXISTS rembo_olap.Sales_Territory
(
    Sales_Territory_Id UInt32,
    Sales_Territory_Country String,
    Sales_Territory_Region String,
    Sales_Territory_City String
)
ENGINE = ReplacingMergeTree
PRIMARY KEY (Sales_Territory_Id)

-- Create the Employee table
CREATE TABLE IF NOT EXISTS rembo_olap.Employee
(
    Employee_Id UInt32,
    Employee_Name String,
    Employee_Territory_Region String
)
ENGINE = ReplacingMergeTree
PRIMARY KEY (Employee_Id)

-- Create the Sales table
CREATE TABLE IF NOT EXISTS rembo_olap.Sales
(
    Sales_Id UInt32,
    CurrencyKey String,
    CustomerKey String,
    Discount_Amount String,
    DueDate String,
    DueDateKey String,
    Extended_Amount String,
    Freight String,
    Order_Date String,
    Order_Quantity String,
    Product_Standard_Cost String,
    Revision_Number String,
    Sales_Amount String,
    Sales_Order_Line_Number String,
    Sales_Order_Number String,
    SalesTerritoryKey String,
    ShipDate String,
    Tax_Amt String,
    Total_Product_Cost String,
    Unit_Price String,
    Unit_Price_Discount_Pct String,
    Employee_Id UInt32,
    Customer_Id UInt32,
    Sales_Territory_Id UInt32
)
ENGINE = ReplacingMergeTree
PRIMARY KEY (Sales_Id)


