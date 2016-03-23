#!/bin/bash

set -euo pipefail
set -x
IFS=$'\n\t'

rm -rf demo_cache.sqlite
./pull_data.py
./pull_oil.sh
./generate_data.sh
./extract_svg.py | tee diagram.svg

