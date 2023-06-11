SELECT
  *
FROM
  tutorial.excel_sql_transaction_data t1
left outer JOIN
  tutorial.excel_sql_inventory_data t2 ON
    (t1.product_id = t2.product_id)