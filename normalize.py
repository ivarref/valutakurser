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

  writer=csv.writer(sys.stdout)
  writer.writerow(available_columns)

  norm = []
  for (idx,row) in enumerate(reader):
    if idx == 0:
      norm = row

    sublist = []
    for (i,x) in enumerate(row):
      if i == 0:
        sublist.append(x)
      elif idx==0:
        sublist.append('100')
      else:
        sublist.append( ((Decimal('100') * Decimal(x)) / Decimal(norm[i])).quantize(Decimal(10) ** -2)) 
    writer.writerow(sublist)
      
