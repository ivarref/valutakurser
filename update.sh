#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

rm -rf demo_cache.sqlite
./pull_data.py
./generate_data.sh
rm -rf screens/; gulp screens

