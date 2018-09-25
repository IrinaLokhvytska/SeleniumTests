from http.server import BaseHTTPRequestHandler, HTTPServer
from app.service_resource import home, page404


class MyServer:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start_server(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.server_close()


class MyHandler(BaseHTTPRequestHandler):
    """ Class for the HTTPServer Handler"""

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/': {
                'status': 200,
                'method': home
            }
        }
        if self.path in paths:
            method = paths[self.path]['method']
            self.respond(paths[self.path], method)
        else:
            self.respond({'status': 404}, page404)

    def handle_http(self, status_code, method):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = method()
        return bytes(content, 'UTF-8')

    def respond(self, opts, method):
        response = self.handle_http(opts['status'], method)
        self.wfile.write(response)
