import socket
import datetime
import errno
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

            print('Received data: {}'.format(data))
            # ここで複数回実行されている
            return data
        except UnicodeDecodeError:
            return None
        except Exception as e:
            pass

    # def test_finish(self):
    #     try :
    #         # 受信バッファを作成
    #         data, cli_addr = self.sock.recvfrom(1024)

    #         data=data.decode('utf-8')

    #         # dataのlenと中身をprintする
    #         print('Received data: {}'.format(data))
            
    #         if data=="true":
    #             return True
            
    #         if data=="false":
    #             return False
            
    #         if data is None:
    #             print('data is None')
            
    #     except KeyboardInterrupt:
    #         print ('\\n . . .\\n')
    #         self.sock.close()
    #         return None
    #     except UnicodeDecodeError:
    #         print('UnicodeDecodeError')
    #         return False
    # # ここにエラーが発生した場合の処理を記述
    #     except Exception as e:
    #         pass

    def close(self):
        self.sock.close()

# udp_receive=UDPReceive(os.environ['MATSUKI7_IP'], 12345)
# while True:
#     try:
#         result=udp_receive.get_conv_start_flg()
#         print(result)
#     except KeyboardInterrupt:
#         break
# udp_receive=UDPReceive('127.0.0.1', 12345)
# test=udp_receive.test_finish()
# print(test)

# データを受け取るまでループする、データを受け取ったらループを抜ける
# while True:
#     date=UDPReceive('127.0.0.1', 12345).get_end_time()

#     if date is not None:
#         # dateを日付型に変換
#         result=datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S.%f')

#         # resultの%fを削除
#         result=result.strftime('%Y/%m/%d %H:%M:%S')
#         print(result)
#         break


