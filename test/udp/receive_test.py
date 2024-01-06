import socket

def udp_server(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))
    sock.settimeout(5)

    try:
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                print(f"Received message: {data.decode()} from {addr}")
            except socket.timeout:
                print("No data received in the last 5 seconds")
    except KeyboardInterrupt:
        print("Server is shutting down")

udp_server('', 12345)
