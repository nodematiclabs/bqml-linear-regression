#standardSQL
CREATE OR REPLACE MODEL `it_help_desk.cases_closed_30d`
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['Cases_Closed']) AS
SELECT
  UNIX_DATE(PARSE_DATE('%b %d, %Y', `Date`)) AS published_days_from_epoch,
  Cases_Closed
FROM
  `it_help_desk.data`
WHERE PARSE_DATE('%b %d, %Y', `Date`) > DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)