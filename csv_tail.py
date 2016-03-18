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

  n = 120
  for arg in sys.argv:
    if arg.startswith('-n='):
      n = int(arg.split('-n=')[1])
  sys.stderr.write("Keeping last %d lines\n" %  (n))

  rows = []
  for row in reader:
    rows.append(row)
    if len(rows) == n+1:
      rows = rows[1:]

  for row in rows:
    writer.writerow(row)


