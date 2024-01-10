import socket
import errno
import struct
import os
from dotenv import load_dotenv
load_dotenv()

class UDPReceive():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.locaddr = (host, port)
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        print('create socket')

    def is_sleepy(self):
        try :
            # 受付待ち
            print('Waiting data...')
            data, cli_addr = self.sock.recvfrom(1024)
            # bool型に変換
            data = struct.unpack('?', data)[0]

            return data
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            return None

    def get_coordinates(self):
        try :
            # 受付待ち
            print('Waiting data...')
            # 途中で強制終了できるようにする
            self.sock.settimeout(20)

            # 受信
            data, cli_addr = self.sock.recvfrom(1024)

            coordinates_result=[]
            for i in range(0, len(data), 8):
                num = struct.unpack('d', data[i:i+8])[0]
                coordinates_result.append(num)
            
            print('Received data: {}'.format(coordinates_result))
            return coordinates_result
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            return None
    
    def is_finish_speaking(self,file,q):
        try :
            # 途中で強制終了できるようにする
            self.sock.settimeout(20)

            # 受信バッファを作成
            buffer = bytearray(1024)

            # 受信
            nbytes, cli_addr = self.sock.recvfrom_into(buffer)

            # nbytesバイトのデータを取得
            data = buffer[:nbytes]
            
            # 音声ファイルの書き込み
            file.write(q.get())

            # bool型に変換
            if len(data)>=1:
                data = struct.unpack('?', data)[0]

                # dataのlenと中身をprintする
                print('Received data: {}'.format(data))
                return data
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            return None
        except Exception as e:
            pass

    def close(self):
        self.sock.close()

# udp_receive=UDPReceive('127.0.0.1', 12345)
# while True:
#     if udp_receive.is_finish_speaking():
#         break
# udp_receive=UDPReceive(os.environ['MATSUKI7_IP'], 12345)
# while True:
#     if udp_receive.is_finish_speaking():
#         break

