from app.api import MyHandler, MyServer

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

if __name__ == '__main__':
    server = MyServer(HOST_NAME, PORT_NUMBER, MyHandler)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
