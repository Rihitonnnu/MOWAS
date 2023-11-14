import os
import logging
from dotenv import load_dotenv
import openai
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from langchain.chat_models import ChatOpenAI
import logging
from SyntheticVoice import SyntheticVoice
from sql import Sql
import rec_unlimited
from gpt import Gpt
import beep


def conversation():
    logger = logging.getLogger(__name__)
    logger.setLevel(10)
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    fh = logging.FileHandler('../log/conversation.log',
                             encoding='utf-8', mode='w')
    logger.addHandler(fh)
    formatter = logging.Formatter('%(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    load_dotenv()

    openai.api_key = os.environ["OPENAI_API_KEY"]

    syntheticVoice = SyntheticVoice()

    user_name = Sql().select('''
                    SELECT  name 
                    FROM    users
                    ''')
    summary = Sql().select('''
                    SELECT  summary 
                    FROM    users
                    ''')

    if user_name != None:
        template = """あなたはドライバーと会話をしながら覚醒を維持するシステムであり、名前はもわすです。
        # 成約条件
        - 会話内容をもとにドライバーに発話を促す質問を行う
        - 最初はどのような話題でお話しますか？と問いかけをする
        
        以下が会話の要約内容です。参考にしてください
        {summary}

        {chat_history}
        Human: {human_input}
        """

    if user_name == None:
        template = """あなたはドライバーの覚醒を維持するシステムであり、名前はもわすです。自分の名前を呼ぶときはもわすと呼んでください。
        また以下が前回の会話の要約内容です。会話を進める上での参考にしてください。
        {summary}
        
        {chat_history}
        Human: {human_input}
        """

    human_template = "{text}"

    prompt = PromptTemplate(
        input_variables=["chat_history", "summary", "human_input"], template=template
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history", input_key="human_input")

    llm = ChatOpenAI(temperature=0.1)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )

    if user_name != None:
        response = llm_chain.predict(
            human_input="こんにちは。あなたの名前はなんですか？私の名前は{}です。".format(user_name), summary=summary)
    else:
        response = llm_chain.predict(
            human_input="こんにちは。あなたの名前はなんですか？名前の登録をしたいです")
    syntheticVoice.speaking(response.replace('AI: ', '').replace('もわす: ', ''))
    print(response.replace('AI: ', ''))

    human_input = rec_unlimited.recording_to_text()
    # human_input = input("You: ")
    logger.info(user_name + ": " + human_input)
    response = llm_chain.predict(human_input=human_input, summary=summary)
    logger.info(response.replace('AI: ', ''))

    syntheticVoice.speaking(response.replace('AI: ', '').replace('もわす: ', ''))
    human_input = rec_unlimited.recording_to_text()
    # human_input = input("You: ")
    logger.info(user_name + ": " + human_input)

    while True:
        try:
            response = llm_chain.predict(
                human_input=human_input, summary=summary)
            logger.info(response.replace('AI: ', ''))
            syntheticVoice.speaking(response.replace(
                'AI: ', '').replace('もわす: ', ''))
            human_input = rec_unlimited.recording_to_text()
            # human_input = input("You: ")
            logger.info(user_name + ": " + human_input)
        except KeyboardInterrupt:
            syntheticVoice.speaking("会話を終了しています。しばらくお待ち下さい ")
            summary = Gpt().make_conversation_summary()
            Sql().store_conversation_summary(summary)
            Sql().store_conversation()
            beep.high()
            exit(1)
