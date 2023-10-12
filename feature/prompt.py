from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


class Prompt:
    def __init__(self):
        pass

    def make_conversation_summary(self):
        with open("../log/conversation.log", encoding="UTF-8") as f:
            conversation_log = f.read()
            prompt = f"""
                    # 命令
                    以下の会話内容を要約しどのような話題について話していたか教えてください

                    {conversation_log}
                    """
            return prompt


Prompt().make_conversation_summary()
