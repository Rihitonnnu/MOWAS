import socket
import time
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
        print('Waiting message')
        data, cli_addr = sock.recvfrom(1024)

        coordinates_result=[]
        for i in range(0, len(data), 8):
            num = struct.unpack('d', data[i:i+8])[0]
            coordinates_result.append(num)
        
        print('Received message: {}'.format(coordinates_result))

        # Clientが受信待ちになるまで待つため
        time.sleep(1)

        # Clientへ受信完了messageを送信
        message = input()
        sock.sendto(message.encode(encoding='utf-8'), cli_addr)
        print('Send response to Client')
    except KeyboardInterrupt:
        print ('\\n . . .\\n')
        sock.close()
        break
