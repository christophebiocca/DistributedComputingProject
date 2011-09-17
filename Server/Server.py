#!/usr/bin/python3
import subprocess
import sys
import http
import http.server
import cgi
import urllib

def MyClosure():
    processed = [0]
    results = []

    class MyRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.endswith("results.txt"):
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(results).encode("utf-8"))
            else:
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                range = (str(processed[0]) + "\n" + str(processed[0] + 10)).encode("utf-8")
                processed[0] += 10
                self.wfile.write(range)
            return

        def do_POST(self):
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })
            results.append(form.getvalue("matchedValue"))

            self.send_response(200)
            self.end_headers()
            self.wfile.write("<HTML>POST OK</HTML>".encode("utf-8"))

    return MyRequestHandler

server = http.server.HTTPServer(('', 80), MyClosure())
print("Started server")
server.serve_forever()
print("end")
