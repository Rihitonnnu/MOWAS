import os
import logging
from dotenv import load_dotenv
import openai

import SyntheticVoice
import logging

import rec_unlimited

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
        logger.info(response)
        logger.info(response.choices[0]["message"]["content"].strip())
        syntheticVoice.speaking(
            response.choices[0]["message"]["content"].strip())

    def conversation(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=70,
        )
        logger.info(response)
        logger.info(response.choices[0]["message"]["content"].strip())
        return response.choices[0]["message"]["content"].strip()

    def continue_conversation(self):
        while True:
            try:
                user_input = rec_unlimited.recording_to_text()
                self.conversation_history += f"{user_input}"

                response = self.conversation(self.conversation_history)
                syntheticVoice.speaking(response)
                print(f"{response}")
                self.conversation_history += f"{response}"
            except KeyboardInterrupt:
                exit(1)


syntheticVoice = SyntheticVoice.SyntheticVoice()
Conversation = Conversation(syntheticVoice)
Conversation.continue_conversation()
