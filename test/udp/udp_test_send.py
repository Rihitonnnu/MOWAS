import socket
import os
from dotenv import load_dotenv
load_dotenv()


def udp_client(message, server_ip, server_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (server_ip, server_port))
            sock.close()
        except KeyboardInterrupt:
            break
        except Exception as e:
            break

udp_client("Hello, Server!", '127.0.0.1', 12345)
# udp_client("Hello, Server!", os.environ["SCHOOL_MACHINE_IP"], 12345)
