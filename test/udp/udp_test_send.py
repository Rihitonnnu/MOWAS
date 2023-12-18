import socket
import os
from dotenv import load_dotenv
load_dotenv()


def udp_client(message, server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (server_ip, server_port))


udp_client("Hello, Server!", os.environ["SCHOOL_MACHINE_IP"], 12345)
