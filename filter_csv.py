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

  if len(sys.argv)!=2:
    sys.stderr.write("Too few arguments. Please specify columns to keep.\n")
    sys.stderr.write("Available columns: %s\n" % (",".join(available_columns)))
    sys.stderr.write("Usage: %s columns\n" % (sys.argv[0]))
    sys.exit(1)

  columns = sys.argv[-1].split(",")
  sys.stderr.write("Keeping colums '%s'\n" % (",".join(columns)))

  writer=csv.writer(sys.stdout)
  writer.writerow(columns)
  for row in reader:
    sublist = [x for (idx,x) in enumerate(row) if available_columns[idx] in columns]
    writer.writerow(sublist)


