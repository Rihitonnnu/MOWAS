import os
import logging
from dotenv import load_dotenv

import openai

logging.basicConfig(filename='Log.txt', filemode='w', level=logging.DEBUG)
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


class Conversation:
    def __init__(self):
        self.conversation_history = "あなたの名前はMOWASです。まずユーザーに名前を聞いて下さい。そしてその名前を記憶し、定期的に名前を呼びかけながら会話を続けて下さい。"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": self.conversation_history
                },
            ],
        )
        print(response.choices[0]["message"]["content"].strip())

    def conversation(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=50,
        )
        logging.debug(response.choices[0]["message"]["content"].strip())
        return response.choices[0]["message"]["content"].strip()

    # 会話を開始するためのメソッド。ここで設定する

    # 名前を聞くような命令を加える→命令が実行され、得られたtxtから名前のみをDBに保存する

    # ques DBからプロンプトに活かしていけばよいか

    def continue_conversation(self):
        while True:
            user_input = input("あなた: ")
            self.conversation_history += f"\nuser: {user_input}"
            response = self.conversation(self.conversation_history)
            print(f"{response}")
            self.conversation_history += f"\nMOWAS: {response}"


Conversation = Conversation()
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

# # 名前を聞くような命令を加える→命令が実行され、得られたtxtから名前のみをDBに保存する

# # ques DBからプロンプトに活かしていけばよいか

# # レスポンスを表示
# print(response.choices[0]["message"]["content"].strip())
