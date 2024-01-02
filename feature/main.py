
from conversation import Conversation
import os
import view.option_window
import udp.udp_receive

try:
    os.mkdir('../sound')
except FileExistsError:
    pass

try:
    os.mkdir('../log')
except FileExistsError:
    pass

# # 眠くなりかけるまで待機
# while True:
#     is_sleepy=udp.udp_receive.UDPReceive('127.0.0.1',2002).is_sleepy()

#     if is_sleepy:
#         break

Conversation().run()
