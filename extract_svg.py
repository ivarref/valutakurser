#!/usr/local/bin/python

# do $ pip install selenium
# if you don't already have selenium python drivers

from selenium import webdriver
import SimpleHTTPServer
import SocketServer
import socket
from threading import Thread
from time import sleep
import sys

class MyTCPServer(SocketServer.TCPServer):
  def server_bind(self):
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)

def run_server(httpd):
  httpd.serve_forever()

if __name__=="__main__":
  PORT = 8080
  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  httpd = MyTCPServer(("", PORT), Handler)
  sys.stderr.write("serving at port %d\n" % (PORT))
  thread = Thread(target = run_server, args = (httpd, ))
  thread.start()
  sleep(1)
  sys.stderr.write("web server running in background\n")

  driver = webdriver.Chrome()
  try:
    driver.get("http://localhost:%d/public/index.html" % (PORT))
    elem = driver.find_element_by_tag_name("svg")
    print elem.get_attribute('innerHTML')
  finally:
    driver.close()
    driver.quit()
    sys.stderr.write("requesting shutdown of web server ...\n")
    httpd.shutdown()
    thread.join()
    sys.stderr.write("requesting shutdown of web server ... OK\n")

