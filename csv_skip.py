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

  n = -1
  for arg in sys.argv:
    if arg.startswith('-n='):
      n = int(arg.split('-n=')[1])
  sys.stderr.write("Skipping first %d lines\n" %  (n))

  for (idx,row) in enumerate(reader):
    if (idx+1)>n:
      writer.writerow(row)


