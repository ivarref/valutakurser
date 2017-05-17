#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

FROM="2013-01-01"

cat monthly_brent.csv | \
  ./rename_column.py "DATE=>date,VALUE=>Oil Price Brent" | \
    ./mma.py | \
    ./csv_from_date.py $FROM | \
    tee monthly_brent_mma.csv | \
    ./normalize.py | \
    tee monthly_brent_mma_normalized.csv

cat valuta_mnd.csv | \
    ./transform_date.py Date "%b-%y" "%Y-%m-%d" | \
    ./csv_skip.py -n=468 | \
    ./filter_csv.py "Date,1 USD,1 EUR,1 GBP" | \
    ./rename_column.py "100 SEK=>SEK,1 USD=>USD,1 EUR=>EUR,1 GBP=>GBP,Date=>date" | \
    ./mma.py | \
    ./csv_from_date.py $FROM | \
    tee valuta_mma.csv | \
    ./normalize.py | \
    ./csv_join.py monthly_brent_mma_normalized.csv | \
    tee public/data.csv

