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
        
        #grab a list of all of the names of the members of the PostRequestMethods module
        memberListNames = dir(PostRequestMethods)
            
        #get the actual members in the list, rather than just strings reflecting the names
        memberList = map(lambda x:getattr(PostRequestMethods, x), memberListNames)
           
        #filter out all but the methods of the member list (i.e. remove the variables and builtins)
        callableMethodList = list(filter(callable,memberList))
            
        #grab the requested method
        requestedMethods = list(filter(lambda x:x.__name__ == requestType, callableMethodList))

        if len(requestedMethods) != 1:
            print("Client attempted to call a method that doesn't exist or has multiple matches: ", requestType)
            return
            
        #call it:
        requestedMethods[0](self, form)\

def main():
    server = http.server.HTTPServer(('', 1080), MyRequestHandler)
    print("Started server")
    server.serve_forever()

if __name__ == "__main__":
    main() 
