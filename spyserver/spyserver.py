#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl, os

certPath = "cert.pem"
dirName  = os.path.dirname(__file__)

if (dirName):
    certPath = "%s/%s" % (dirName,certPath)

class CORSRequestHandler(SimpleHTTPRequestHandler):
        def end_headers(self):
                self.send_header('Access-Control-Allow-Origin','*')
                SimpleHTTPRequestHandler.end_headers(self)

httpd = HTTPServer(('localhost', 31337), CORSRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=certPath, server_side=True)
httpd.serve_forever()