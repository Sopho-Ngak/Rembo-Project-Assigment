/*
Here are example SQL queries that we can use in Power BI to address the specific reporting needs mentioned in the context:

Sales by Employee:
*/

SELECT
    e.Employee_Name,
    SUM(s.Sales_Amount) AS TotalSales
FROM
    Sales s
JOIN
    Employee e ON s.Employee_Id = e.Employee_Id
GROUP BY
    e.Employee_Name
ORDER BY
    TotalSales DESC

-- Top 100 Customers - Average Purchase Time and Price:
SELECT
    c.Customer_Id,
    c.Last_Name,
    AVG(DATEDIFF('day', TODate(c.Date_First_Purchase), TODate(s.Order_Date))) AS AvgPurchaseTime,
    AVG(s.Sales_Amount) AS AvgPurchasePrice
FROM
    Sales s
JOIN
    Customer c ON s.CustomerKey = c.Customer_Id
GROUP BY
    c.Customer_Id, c.First_Name, c.Last_Name
ORDER BY
    AvgPurchasePrice DESC
LIMIT 100

-- Year-over-Year Change of Sales:
SELECT
    YEAR(s.Order_Date) AS SalesYear,
    SUM(s.Sales_Amount) AS TotalSales
FROM
    Sales s
GROUP BY
    SalesYear
ORDER BY
    SalesYear

--- Real-time Sales by Region and Country:

SELECT
    st.Sales_Territory_Region,
    st.Sales_Territory_Country,
    SUM(s.Sales_Amount) AS TotalSales
FROM
    Sales s
JOIN
    Sales_Territory st ON s.Sales_Territory_Id = st.Sales_Territory_Id
GROUP BY
    st.Sales_Territory_Region, st.Sales_Territory_Country
