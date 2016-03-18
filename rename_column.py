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
  
  if len(sys.argv)==1:
    sys.stderr.write('Usage: %s "old=>new,old2=>new2"\n' % (sys.argv[0]))
    sys.exit(1)
  rename = sys.argv[-1].split(",")
  
  writer=csv.writer(sys.stdout)
  sublist = []
  for col in available_columns:
    found = False
    for x in rename:
      (frm,to) = x.split("=>")
      if col == frm:
        sublist.append(to)
        found = True
    if not found: 
      sublist.append(col)
  writer.writerow(sublist)
  for row in reader:
    writer.writerow(row)



