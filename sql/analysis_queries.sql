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