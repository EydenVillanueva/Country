#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer

#from server import Server

PORT = 8080
HOST = 'localhost'

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    def do_POST(self):
        return
    def do_GET(self):
        self.respond()

    def handle_http(self,status,content_type):

        self.send_response(status)
        self.send_header('Content-type',content_type)
        self.end_headers()

        f = open('response.json',encoding='utf-8')
        content = f.read()
        f.close()

        return bytes(content,'UTF-8')

    def respond(self):
        content = self.handle_http(200, 'application/json')
        self.wfile.write(content)


if __name__ == '__main__':

    httpd = HTTPServer((HOST,PORT), Handler)
    print('Server Started... at {} : {} '.format(HOST,PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt Ctrl + C')