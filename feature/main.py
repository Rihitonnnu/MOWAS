
import feature.conversation as conversation
import os
import view.option_window
view.option_window

try:
    os.mkdir('../sound')
except FileExistsError:
    pass

try:
    os.mkdir('../log')
except FileExistsError:
    pass

conversation.conversation()
