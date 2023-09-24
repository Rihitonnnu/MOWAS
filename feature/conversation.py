import os
import logging
from dotenv import load_dotenv
import openai

import SyntheticVoice
import speechRecognition
import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)
sh = logging.StreamHandler()
logger.addHandler(sh)
fh = logging.FileHandler('../log/conversation.log', encoding='utf-8')
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


class Conversation:
    def __init__(self, syntheticVoice):
        self.conversation_history = "あなたの名前はもわすです。自分の名前を呼ぶときはもわすと呼んでください。まずユーザーに名前を聞いて下さい。そしてその名前を記憶し、定期的に名前を呼びかけながら会話を続けて下さい。"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": self.conversation_history
                },
            ],
        )
        logger.info(
            response.choices[0]["message"]["content"].strip())
        syntheticVoice.speaking(
            response.choices[0]["message"]["content"].strip())
        # print(response.choices[0]["message"]["content"].strip())

    def conversation(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=50,
        )
        logger.info(
            response.choices[0]["message"]["content"].strip())
        return response.choices[0]["message"]["content"].strip()

    # 名前を聞くような命令を加える→命令が実行され、得られたtxtから名前のみをDBに保存する
    # ques DBからプロンプトに活かしていけばよいか

    def continue_conversation(self):
        while True:
            # ここで音声で入力を行う→漢字変換しないほうがよき？
            print(speechRecognition)
            user_input = speechRecognition()
            print(user_input)
            self.conversation_history += f"{user_input}"
            response = self.conversation(self.conversation_history)
            syntheticVoice.speaking(response)
            print(f"{response}")
            self.conversation_history += f"{response}"


# メソッド実行
syntheticVoice = SyntheticVoice.SyntheticVoice()
Conversation = Conversation(syntheticVoice)
Conversation.continue_conversation()


# # 標準入力と改行
# userSpeech = input()
# print()

# # 会話履歴によってここは分岐する
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "あなたは居眠り防止システムMOWASです。まずユーザーに名前を聞いて下さい。"
#         },
#         {"role": "user", "content": userSpeech},
#     ],
# )
