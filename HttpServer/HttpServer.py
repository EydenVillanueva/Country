#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import json
from urllib.parse import urlparse,parse_qs

sys.path.append('../Country')
from api import CountryApi

#from server import Server

PORT = 8080
HOST = 'localhost'

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    def do_POST(self):
        return
    def do_GET(self):
        
        code = parse_qs(urlparse(self.path).query).get('country',None)[0]
        print(code)
        if code:
            country = CountryApi(code)
            result = json.dumps(country.get_dict())
        else:
            result = '{}'
        
        self.respond(result)

    def handle_http(self,status,content_type,content):

        self.send_response(status)
        self.send_header('Content-type',content_type)
        self.end_headers()

        return bytes(content,'UTF-8')

    def respond(self,result):
        content = self.handle_http(200, 'application/json',result)
        self.wfile.write(content)


if __name__ == '__main__':

    httpd = HTTPServer((HOST,PORT), Handler)
    print('Server Started... at {} : {} '.format(HOST,PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt Ctrl + C')