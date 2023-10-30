from SyntheticVoice import SyntheticVoice
from gpt import Gpt
from sql import Sql
import beep


class Command:
    def __init__(self, command):
        self.command = command

    def command_execute(self):
        if (self.command == "会話終了"):
            SyntheticVoice().speaking("会話を終了しています。しばらくお待ち下さい ")
            summary = Gpt().make_conversation_summary()
            Sql().store_conversation_summary(summary)
            beep.high()
            exit(1)
