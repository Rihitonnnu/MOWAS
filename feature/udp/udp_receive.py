import socket
import struct

class UDPReceive():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.locaddr = (host, port)
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        print('create socket')

    def get_eor(self):
        try :
            # 受付待ち
            print('Waiting data...')
            data, cli_addr = self.sock.recvfrom(1024)
            # dataを浮動小数点数に変換
            data = struct.unpack('dd', data)

            print('Received data: {}'.format(data[0]))
            print('Received data: {}'.format(data[1]))
            return data
        except KeyboardInterrupt:
            print ('\\n . . .\\n')
            self.sock.close()
            return None

    def get_coordinates(self):
        try :
            # 受付待ち
            print('Waiting data...')
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

    def close(self):
        self.sock.close()

UDPReceive('127.0.0.1',2002).get_eor()
# UDPReceive('127.0.0.1',2002).get_coordinates()
