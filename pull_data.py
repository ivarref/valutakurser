#!/usr/local/bin/python

if __name__=="__main__":
  import requests_cache
  import requests
  from lxml import html
  requests_cache.install_cache('demo_cache')
  page = requests.get("http://www.norges-bank.no/en/Statistics/exchange_rates/")
  tree = html.fromstring(page.content)
  m = tree.xpath('.//a[text()="Monthly exchange rates (from 1960)" and contains(@href, "csv")]')[0]
  url = m.attrib['href']
  print "Downloading %s" % (url)
  r = requests.get(url)
  with open('valuta_mnd.csv', 'wb') as fd:
    for line in r.content.split("\n"):
      if line.strip() == "":
        continue
      fd.write(line.strip())
      fd.write("\n")

