from app.api import MyHandler, MyServer
from config import HOST_NAME, PORT_NUMBER


if __name__ == '__main__':
    server = MyServer(HOST_NAME, PORT_NUMBER, MyHandler)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
