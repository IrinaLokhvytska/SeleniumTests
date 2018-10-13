from app.api import MyHandler, MyServer
from config import Config


if __name__ == '__main__':
    config = Config()
    server = MyServer(config.host_name, config.port_number, MyHandler)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
