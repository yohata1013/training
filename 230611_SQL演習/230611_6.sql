with inventory_data AS(
  SELECT
    product_id,
    product_name,
    current_inventory
  FROM
    tutorial.excel_sql_inventory_data
  group BY
    1,2,3
)

,transaction_data as(
  SELECT
    product_id,
    count(transaction_id) as transaction
  FROM
    tutorial.excel_sql_transaction_data
  group BY
    1
)

--ジョインする
,join_cal as(
  SELECT
    t1.*,
    t2.transaction
  FROM
    inventory_data t1
  INNER JOIN
    transaction_data t2 ON
      (t1.product_id = t2.product_id)
)

--計算する
,cal as(
SELECT
  *,
  (current_inventory - transaction) as cal
FROM
  join_cal)
  
SELECT
  product_id,
  product_name,
  cal
FROM
  cal
WHERE
  cal<0
order BY
  1