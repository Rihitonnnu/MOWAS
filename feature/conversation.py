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
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from SyntheticVoice import SyntheticVoice
from sql import Sql
import rec_unlimited


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

    user_name = Sql().select_name()

    if user_name != None:
        template = """あなたはドライバーの覚醒を維持するシステムであり、名前はもわすです。自分の名前を呼ぶときはもわすと呼んでください。
        ユーザーの入力から得られた名前を定期的に呼びかけながら会話を行ってください。
        また操作のオプションは２つあります。名前の更新と会話です。
        名前の更新は現在のユーザーの名前と登録されている名前と異なる名前の場合に適切な名前の登録を行います。
        {chat_history}
        Human: {human_input}
        """

    if user_name == None:
        template = """あなたはドライバーの覚醒を維持するシステムであり、名前はもわすです。自分の名前を呼ぶときはもわすと呼んでください。
        まず名前の登録を行ってください。名前を登録する場合はコントロールNボタンを押して名前を言ってもらうように案内してください
        {chat_history}
        Human: {human_input}
        """

    human_template = "{text}"

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template
    )
    memory = ConversationBufferMemory(memory_key="chat_history")

    llm = ChatOpenAI(temperature=0.1)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory
    )

    if user_name != None:
        response = llm_chain.predict(
            human_input="こんにちは。あなたの名前はなんですか？私の名前は{}です。".format(user_name))
    else:
        response = llm_chain.predict(
            human_input="こんにちは。あなたの名前はなんですか？名前の登録をしたいです")
    syntheticVoice.speaking(response[5:])
    print(response[5:])

    # ここrefactorが必要
    # human_input = rec_unlimited.recording_to_text()
    human_input = input("You: ")
    logger.info(user_name + ": " + human_input)
    response = llm_chain.predict(human_input=human_input)
    logger.info(response[4:])

    syntheticVoice.speaking(response[7:])
    # human_input = rec_unlimited.recording_to_text()
    human_input = input("You: ")
    logger.info(user_name + ": " + human_input)

    while True:
        try:
            response = llm_chain.predict(human_input=human_input)
            logger.info(response[4:])
            syntheticVoice.speaking(response[9:])
            # human_input = rec_unlimited.recording_to_text()
            human_input = input("You: ")
            logger.info(user_name + ": " + human_input)
        except KeyboardInterrupt:
            exit(1)
