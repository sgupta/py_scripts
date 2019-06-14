from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import logging
f=open('/home/sgupta3/py_project/deployments', "rb")
file_contents = f.read()
f.close()
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(file_contents)

httpd = HTTPServer(('localhost',4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
        keyfile="/home/sgupta3/key.pem",
        certfile="/home/sgupta3/cert.pem", server_side=True)

httpd.serve_forever()
