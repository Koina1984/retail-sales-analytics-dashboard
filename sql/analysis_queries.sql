-- Total Revenue
SELECT SUM(Revenue)
FROM sales;

-- Revenue by Category
SELECT Category,
SUM(Revenue)
FROM sales
GROUP BY Category;

-- Top Customers
SELECT Customer_ID,
SUM(Revenue) AS TotalRevenue
FROM sales
GROUP BY Customer_ID
ORDER BY TotalRevenue DESC;

-- Monthly Revenue
SELECT Month,
SUM(Revenue)
FROM sales
GROUP BY Month
ORDER BY Month;

-- Profit by Category
SELECT
    Category,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category
ORDER BY TotalProfit DESC;

-- Top 5 Categories by Revenue
SELECT
    Category,
    SUM(Revenue) AS TotalRevenue
FROM sales
GROUP BY Category
ORDER BY TotalRevenue DESC
LIMIT 5;

-- Average Order Value
SELECT
    AVG(Revenue) AS AverageOrderValue
FROM sales;

-- Monthly Profit
SELECT
    Month,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Month
ORDER BY Month;