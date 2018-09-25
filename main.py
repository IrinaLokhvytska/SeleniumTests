from . import app


HOST_NAME = 'localhost'
PORT_NUMBER = 8000
server = app.api.MyServer
handler = app.api.MyHandler

if __name__ == '__main__':
    server = server(HOST_NAME, PORT_NUMBER, handler)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
