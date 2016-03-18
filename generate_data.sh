#!/bin/bash

cat valuta_mnd.csv | \
    ./transform_date.py Date "%b-%y" "%Y-%m-%d" | \
    ./csv_skip.py -n=468 | \
    ./filter_csv.py "Date,100 SEK,1 USD,1 EUR,1 GBP" | \
    ./mma.py | \
    ./csv_tail.py -n=60 | \
    ./normalize.py | \
    ./rename_column.py "100 SEK=>SEK,1 USD=>USD,1 EUR=>EUR,1 GBP=>GBP,Date=>date" | \
    cat > public/data.csv

