/* Challenge 1: Running totals and ranking
For each customer, return every order along with a running total of their 
revenue to date, and their rank among their own orders by revenue (highest first).
*/

-- Working table
SELECT order_id, customer_id, order_date, amount
	FROM dbt_fundamentals.fct_orders;
	
-- Answer:
SELECT
	customer_id,
	order_id,
	order_date,
	amount AS order_amount,
	SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date) AS running_total,
	SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total2,
	DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY amount DESC) AS order_ranking
FROM dbt_fundamentals.fct_orders AS o
ORDER BY customer_id, order_ranking

/* Explanation
Use running_total2 since it explicitly sets the frame for when there are ties within
the partition for the ORDER_BY clause (order_date). Without setting it explicitly (running_total) 
Postgres uses RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW by default.
*/



/* Challenge 2: Deduplication with ROW_NUMBER()
Deduplicate the customers in the fct_order table, use the most recent order date.
*/

-- Working table:
SELECT order_id, customer_id, order_date FROM dbt_fundamentals.fct_orders ORDER BY customer_id;

-- Answer
WITH dups AS (
	SELECT
		customer_id,
		order_date,
		ROW_NUMBER() OVER(
			PARTITION BY customer_id ORDER BY order_date DESC
			ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
		) AS order_ranking
	FROM dbt_fundamentals.fct_orders
)
SELECT customer_id FROM dups
WHERE order_ranking = 1
ORDER BY 1;



/* Challenge 3: Period-over-period growth (self-join)
Calculate month-over-month revenue growth (%) per customer.
*/

-- Working table:
WITH base AS (
	SELECT
		customer_id,
		DATE_TRUNC('month', order_date)::DATE AS order_month,
		amount
	FROM dbt_fundamentals.fct_orders
),
dedup AS (
	SELECT 
		customer_id,
		order_month,
		SUM(amount) AS month_total
	FROM base
	GROUP by customer_id, order_month
	ORDER BY 1, 2 DESC
)
SELECT * FROM dedup

-- Answer:
WITH base AS (
	SELECT
		customer_id,
		DATE_TRUNC('month', order_date)::DATE AS order_month,
		amount
	FROM dbt_fundamentals.fct_orders
),
curr AS (
	SELECT 
		customer_id,
		order_month,
		SUM(amount) AS month_total
	FROM base
	GROUP by customer_id, order_month
)
SELECT
	curr.customer_id,
	curr.order_month,
	curr.month_total AS current_month_total,
	prev.month_total AS previous_month_total,
	( ( (curr.month_total / prev.month_total) - 1) * 100)::INTEGER AS growth
FROM curr
LEFT JOIN curr AS prev
	ON curr.customer_id = prev.customer_id
	AND prev.order_month = curr.order_month - INTERVAL '1 month'
ORDER BY curr.customer_id, curr.month_total

-- Alternate Solution:
--Calculates growth when last month customer bought, not 1 month before current month
WITH base AS (
	SELECT
		customer_id,
		DATE_TRUNC('month', order_date)::DATE AS order_month,
		amount
	FROM dbt_fundamentals.fct_orders
),
dedup AS (
	SELECT 
		customer_id,
		order_month,
		SUM(amount) AS month_total
	FROM base
	GROUP by customer_id, order_month
)
SELECT 
	customer_id,
	order_month,
	month_total,
	LAG(month_total, 1) OVER(PARTITION BY customer_id ORDER BY order_month) AS last_bought_month_total,
	( ( (month_total / LAG(month_total, 1) OVER(PARTITION BY customer_id ORDER BY order_month) ) - 1) * 100)::INTEGER AS growth
-- 	ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_month) rn
FROM dedup
ORDER BY 1, 2



SELECT * FROM dbt_fundamentals.dim_customers;
SELECT * FROM jaffle_shop.customers;