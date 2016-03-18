#!/bin/bash

rm -rf demo_cache.sqlite
./pull_data.py
./generate_data.sh
rm -rf screens/; gulp screens

