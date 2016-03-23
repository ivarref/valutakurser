#!/usr/local/bin/python

import csv
import sys

if __name__=="__main__":
  inf = sys.stdin
  reader = csv.reader(inf)
  available_columns = []
  for row in reader:
    for x in row:
      available_columns.append(x)
    break

  writer=csv.writer(sys.stdout)
  writer.writerow(available_columns)

  for row in reader:
    if row[0] >= sys.argv[-1]:
      writer.writerow(row)
    
