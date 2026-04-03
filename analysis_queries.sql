SELECT 
    Course_Category, 
    SUM(Subscription_Fee) AS Total_Revenue,
    COUNT(User_ID) AS Student_Count
FROM subscriptions
GROUP BY Course_Category
ORDER BY Total_Revenue DESC;

SELECT 
    User_ID, 
    Course_Category, 
    Days_Since_Last_Login
FROM subscriptions
WHERE Days_Since_Last_Login > 20 
  AND Churned = 0
ORDER BY Days_Since_Last_Login DESC
LIMIT 10;

SELECT 
    Subscription_Type,
    AVG(Hours_Watched) AS Avg_Study_Time,
    AVG(Subscription_Fee) AS Avg_Paid
FROM subscriptions
GROUP BY Subscription_Type;