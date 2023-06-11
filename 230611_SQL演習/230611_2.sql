SELECT
  date,
  max(volume) as max_volume
FROM
  tutorial.aapl_historical_stock_price
WHERE
  year= 2013
group BY
  1
LIMIT
  1