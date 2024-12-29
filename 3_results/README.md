### 3_results/README.md

**SQL Queries**

**Count the number of rows**

SELECT COUNT(*) AS row_count
FROM `bigquerycustomers.customers_dataset.cleaned_customers`;

*Description: Counts the total number of rows in the table.*

**Preview the first ten rows**

SELECT *
FROM `bigquerycustomers.customers_dataset.cleaned_customers`
LIMIT 10;

*Description: Retrieves the first ten rows for preview.*

**Group customers by profession and count them**

SELECT Profession, COUNT(*) AS customer_count
FROM `bigquerycustomers.customers_dataset.cleaned_customers`
GROUP BY Profession
ORDER BY customer_count DESC;

*Description: Groups customers by their profession and provides the count, sorted in descending order.*

**Find customers with high spending scores (above ninety)**

SELECT *
FROM `bigquerycustomers.customers_dataset.cleaned_customers`
WHERE `Spending_Score_1_100` > 90;

*Description: Filters customers with spending scores greater than ninety.*

**Group customers by profession and calculate the average spending score**

SELECT Profession, AVG(`Spending_Score_1_100`) AS avg_spending_score
FROM `bigquerycustomers.customers_dataset.cleaned_customers`
GROUP BY Profession
ORDER BY avg_spending_score DESC;

*Description: Calculates the average spending score for each profession, sorted in descending order of the average.*