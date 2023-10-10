
import test_conversation
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

test_conversation.conversation()
