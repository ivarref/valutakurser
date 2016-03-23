#!/bin/bash

DAT="$(python -c "import datetime; today = datetime.date.today(); first = today.replace(day=1); lastMonth = first - datetime.timedelta(days=1); print lastMonth.strftime('%Y-%m-01')")"

curl --data "form[units]=lin&form[frequency]=Monthly&form[aggregation]=Average&form[obs_start_date]=1987-06-01&form[obs_end_date]=$DAT&form[file_format]=csv" https://research.stlouisfed.org/fred2/series/DCOILBRENTEU/downloaddata | tr -d '\r' > monthly_brent.csv

