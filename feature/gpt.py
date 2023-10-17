from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


class Gpt:
    def __init__(self):
        pass

    def make_conversation_summary(self):
        with open("../log/conversation.log", encoding="UTF-8") as f:
            conversation_log = f.read()
            prompt = f"""
                    # 命令
                    以下の会話内容から会話のトピック(単語や会話のテーマ)を教えてください

                    {conversation_log}
                    """
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}],
            )
            return response['choices'][0]['message']['content']
            # print(response['choices'][0]['message']['content'])
