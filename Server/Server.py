import subprocess
import sys
import http
import http.server
import cgi
import urllib
import pickle
import PostRequestMethods

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("results.txt"):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(PostRequestMethods.state.displayData().encode("utf-8"))

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                        'CONTENT_TYPE':self.headers['Content-Type'],
                        })
        
        requestType = form.getvalue("request")
        try:
            list(filter(lambda x:x.__name__ == requestType, list(filter(callable,map(lambda x:getattr(PostRequestMethods, x), dir(PostRequestMethods))))))[0](self, form)
        except IndexError:
            print("Client attempted to call a method that doesn't exist: ", requestType)


def main():
    server = http.server.HTTPServer(('', 1080), MyRequestHandler)
    print("Started server")
    server.serve_forever()

if __name__ == "__main__":
    main()  