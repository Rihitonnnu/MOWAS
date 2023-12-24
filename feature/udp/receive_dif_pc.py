import socket

# Set up UDP socket
UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 5005  # Choose a suitable port number
BUFFER_SIZE = 1024

# Create socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
sock.bind((UDP_IP, UDP_PORT))

# Receive and print incoming data
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print("Received data:", data.decode())
