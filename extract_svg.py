#!/usr/local/bin/python

from selenium import webdriver

import SimpleHTTPServer
import SocketServer

from threading import Thread
from time import sleep

def run_server(httpd):
  httpd.serve_forever()

if __name__=="__main__":
  PORT = 8000
  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  httpd = SocketServer.TCPServer(("", PORT), Handler)
  print "serving at port", PORT
  thread = Thread(target = run_server, args = (httpd, ))
  thread.start()
  sleep(1)
  print "web server running in background"

  driver = webdriver.Chrome()
  try:
    driver.get("http://localhost:8000/public/index.html")
    #import ipdb; ipdb.set_trace()
    pass
  finally:
    driver.close()
    print "requesting shutdown of web server"
    httpd.shutdown()
    thread.join()


