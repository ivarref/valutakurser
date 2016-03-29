#!/usr/local/bin/python

if __name__=="__main__":
  import requests_cache
  import requests
  from lxml import html
  import csv
  import sys
  requests_cache.install_cache('demo_cache')
  page = requests.get("http://factpages.npd.no/ReportServer?/FactPages/TableView/field_production_totalt_NCS_month__DisplayAllRows&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=2.150.58.78&CultureCode=en")
  content = [x.strip() for x in page.content.split("\n") if x.strip() != ""]

  columns = content[0].split(",")[2:]
  columns.insert(0, 'date')

  print ",".join(columns)

  for row in reversed(content[1:]):
    pieces = row.split(",")
    print "%d-%02d-01,%s" % (int(pieces[0]), int(pieces[1]), ",".join(pieces[2:]))

