#!/usr/local/bin/python

from __future__ import division
import csv
import sys
from decimal import Decimal

def firstrow(reader, writer):
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
  
def domax(reader, writer):
  maxx = []
  rows = []
  for (idx,row) in enumerate(reader):
    rows.append(row)

    if idx == 0:
      maxx = [Decimal(x) for x in row[1:]]
      continue
    for (i, c) in enumerate(row[1:]):
      maxx[i] = max(maxx[i], Decimal(c))

  for row in rows:
    sublist = []
    for (i,x) in enumerate(row):
      if i == 0:
        sublist.append(x)
      elif maxx[i-1]==Decimal(x):
        sublist.append('100.00')
      else:
        sublist.append( ((Decimal('100') * Decimal(x)) / Decimal(maxx[i-1])).quantize(Decimal(10) ** -2)) 
    writer.writerow(sublist)

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
      
  if "--max" in sys.argv:
    domax(reader, writer)
  else:
    firstrow(reader, writer)
  
