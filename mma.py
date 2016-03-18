#!/usr/local/bin/python

from __future__ import division
import csv
import sys
from decimal import Decimal

if __name__=="__main__":
  inf = sys.stdin
  reader = csv.reader(inf)
  available_columns = []
  for row in reader:
    for x in row:
      available_columns.append(x)
    break

  columns = available_columns[1:]
  sys.stderr.write("Making 12 moving average for colums '%s'\n" % (",".join(columns)))

  writer=csv.writer(sys.stdout)
  writer.writerow(available_columns)
  mma = []

  for row in reader:
    mma.append(row)
    if len(mma)==12:
      sublist = []
      for (idx, x) in enumerate(row):
        if available_columns[idx] in columns:
          values = [Decimal(r[idx]) for r in mma]
          mean = sum(values) / len(values)
          sublist.append(mean)
        else:
          sublist.append(x)
      writer.writerow(sublist)
      mma = mma[1:]
      
