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

  if len(sys.argv)-1!=3:
    sys.stderr.write("Usage: %s column_name input_format output_format\n" % sys.argv[0])
    sys.exit(1)

  column = sys.argv[1]
  input_format = sys.argv[2]
  output_format = sys.argv[3]
  writer=csv.writer(sys.stdout)
  writer.writerow(available_columns)
  for row in reader:
    sublist = []
    for (idx, x) in enumerate(row):
      if available_columns[idx] == column:
        import locale
        from datetime import datetime
        loc= locale.setlocale(locale.LC_TIME,("en","us"))
        date = datetime.strptime(x, input_format)
        date_str = date.strftime(output_format)
        sublist.append(date_str)
      else:
        sublist.append(x)
    writer.writerow(sublist)
          
