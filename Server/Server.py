import subprocess
import sys
import http
import http.server
import cgi


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write("10\n20".encode("utf-8"))
        return

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            query = cgi.parse_multipart(self.rfile, pdict)
        self.send_response(301)
        self.end_headers()

        upfilecontent = query.get('upfile')
        print("content: ", upfilecontent[0])
        self.wfile.write("<HTML>POST OK</HTML>".encode("utf-8"))
        self.wfile.write(upfilecontent[0].encode("utf-8"))

server = http.server.HTTPServer(('', 1080), MyRequestHandler)
print("Started server")
server.serve_forever()
print("end")


clientInterface = subprocess.Popen(r"dist\Client.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

print(clientInterface.stdin)

clientInterface.stdin.write("10\n".encode("utf-8"))
clientInterface.stdin.write("20\n".encode("utf-8"))

while True:
    line = clientInterface.stdout.readline()
    if line:
        print(int(line))
    else:
        break
