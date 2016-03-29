#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

./pull_oil_production.py | \
  ./filter_csv.py date,prfPrdOilNetMillSm3,prfPrdGasNetBillSm3,prfPrdOeNetMillSm3 | \
  ./rename_column.py "prfPrdOilNetMillSm3=>Oil,prfPrdGasNetBillSm3=>Gas,prfPrdOeNetMillSm3=>Petroleum" | \
  ./mma.py --round | \
  ./normalize.py --max | tee ./public/ncs_value.csv

echo '{ "title" : "Norwegian Continental Shelf Petroleum production. All time high = 100."}' > public/title.json
./extract_svg.py "/public/ncs_value.html" | tee ncs_production_overview.svg



