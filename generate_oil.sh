#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

cat monthly_brent.csv | \
  ./rename_column.py "DATE=>date,VALUE=>Oil Price (Brent)" | \
    ./mma.py | \
    ./csv_tail.py -n=60 | \
    ./normalize.py

