#!/usr/local/bin/python

import csv
import sys

def available_columns_and_reader(inf):
  reader = csv.reader(inf)
  available_columns = []
  for row in reader:
    for x in row:
      available_columns.append(x)
    break
  return (available_columns, reader)
  
if __name__=="__main__":
  (available_columns, reader) = available_columns_and_reader(sys.stdin)

  writer=csv.writer(sys.stdout)

  join_file = sys.argv[-1]
  sys.stderr.write("csv_join.py: joining with file %s\n" % (join_file))
  with open(join_file, 'r') as fd:
    (new_columns, reader2) = available_columns_and_reader(fd)
    if available_columns[0] != new_columns[0]:
      sys.stderr.write("expected first column to match\n")
      sys.exit(1)
    available_columns.extend(new_columns[1:])
    writer.writerow(available_columns)
    for row in reader:
      for r in reader2:
        if row[0] != r[0]:
          sys.stderr.write("expected first column to match\n")
          sys.exit(1)
        row.extend(r[1:])
        writer.writerow(row)
        break
      pass

