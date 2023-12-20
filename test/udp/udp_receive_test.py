import socket
import struct

# 自分のPCのアドレスとport.
host = '127.0.0.1'
port = 2002
locaddr = (host, port)

# ソケットを作成する
sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
print('create socket')

# 自ホストで使用するIPアドレスとポート番号を指定
sock.bind(locaddr)

while True:
    try :
        # 受付待ち
        print('Waiting data...')
        data, cli_addr = sock.recvfrom(1024)

        coordinates_result=[]
        for i in range(0, len(data), 8):
            num = struct.unpack('d', data[i:i+8])[0]
            coordinates_result.append(num)
        
        print('Received data: {}'.format(coordinates_result))
    except KeyboardInterrupt:
        print ('\\n . . .\\n')
        sock.close()
        break
