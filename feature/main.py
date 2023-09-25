import conversation
import os

try:
    os.mkdir('../sound')
except FileExistsError:
    pass

try:
    os.mkdir('../log')
except FileExistsError:
    pass

conversation.Conversation()
