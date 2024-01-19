import socket
import datetime
import struct
import os
from dotenv import load_dotenv
import ast
load_dotenv()

class UDPReceive():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.locaddr = (host, port)
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)

    def is_sleepy(self):
        try :
            # 受付待ち
            data, cli_addr = self.sock.recvfrom(1024)
            # bool型に変換
            data = struct.unpack('?', data)[0]
            return data
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            exit(1)
            return None

    # 緯度経度を取得
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
    
    def get_conv_start_flg(self):
        try :
            # 受信バッファを作成
            data, cli_addr = self.sock.recvfrom(1024)
            self.sock.settimeout(10)

            # dataを文字列に変換
            data=data.decode('utf-8')
            
            print('Received data: {}'.format(data))
            data = ast.literal_eval(data)
            
            return data
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            return None
        except Exception as e:
            pass
    
    # udpで送信された時刻を取得
    def get_end_time(self):
        try :
            # 受信バッファを作成
            data, cli_addr = self.sock.recvfrom(1024)
            self.sock.settimeout(10)

            # dataを文字列に変換
            data=data.decode('utf-8')
            reaction_time=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
            print('Received data: {}'.format(reaction_time))

            return reaction_time
        except UnicodeDecodeError:
            return None
        except Exception as e:
            pass

    def get_rec_start_flg(self):
        try :
            # 受信バッファを作成
            data, cli_addr = self.sock.recvfrom(1024)
            self.sock.settimeout(10)

            # dataを文字列に変換
            data=data.decode('utf-8')

            print('Received data: {}'.format(data))
            # ここで複数回実行されている
            return data
        except UnicodeDecodeError:
            return None
        except Exception as e:
            pass

    def close(self):
        self.sock.close()
