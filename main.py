from http.server import HTTPServer
from app.api import MyHandler

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
