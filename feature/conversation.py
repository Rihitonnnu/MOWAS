import os
import logging
from dotenv import load_dotenv
import openai
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
import logging
from SyntheticVoice import SyntheticVoice
from sql import Sql
import rec_unlimited
from gpt import Gpt
import beep
import key_extraction
import log_instance
from token_record import TokenRecord


def conversation():
    # ログの設定
    logger = log_instance.log_instance('conversation')

    # 環境変数読み込み
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]

    syntheticVoice = SyntheticVoice()
    token_record = TokenRecord()

    # SQLクエリ設定
    user_name = Sql().select('''
                    SELECT  name 
                    FROM    users
                    ''')
    summary = Sql().select('''
                    SELECT  summary 
                    FROM    users
                    ''')

    # テンプレート,プロンプトの設定
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

    # 記憶するmemoryの設定
    memory = ConversationBufferWindowMemory(
        k=1, memory_key="chat_history", input_key="human_input")

    llm = ChatOpenAI(temperature=0.1)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )

    with get_openai_callback() as cb:
        # 会話回数を初期化
        conv_cnt = 1

        # 事前に入力をしておくことでMOWAS側からの応答から会話が始まる
        # 分岐はドライバーの名前が入力されているかどうか
        if user_name != None:
            response = llm_chain.predict(
                human_input="こんにちは。あなたの名前はなんですか？私の名前は{}です。".format(user_name), summary=summary)
        else:
            response = llm_chain.predict(
                human_input="こんにちは。あなたの名前はなんですか？名前の登録をしたいです")
        syntheticVoice.speaking(response.replace(
            'AI: ', '').replace('もわす: ', ''))
        print(response.replace('AI: ', ''))

        # トークンをexcelに記録
        token_record.token_record(cb, conv_cnt)
        conv_cnt += 1

        # 利用者が初めて発話、それに対する応答
        # human_input = rec_unlimited.recording_to_text()
        human_input = input("You: ")
        logger.info(user_name + ": " + human_input)
        response = llm_chain.predict(human_input=human_input, summary=summary)
        logger.info(response.replace('AI: ', ''))
        syntheticVoice.speaking(response.replace(
            'AI: ', '').replace('もわす: ', ''))
        print(cb)
        exit(1)

        # human_input = rec_unlimited.recording_to_text()
        human_input = input("You: ")
        logger.info(user_name + ": " + human_input)

        while True:
            try:
                response = llm_chain.predict(
                    human_input=human_input, summary=summary)
                logger.info(response.replace('AI: ', ''))
                syntheticVoice.speaking(response.replace(
                    'AI: ', '').replace('もわす: ', ''))
                # human_input = rec_unlimited.recording_to_text()
                key_extraction(human_input)
                human_input = input("You: ")
                logger.info(user_name + ": " + human_input)
            except KeyboardInterrupt:
                syntheticVoice.speaking("会話を終了しています。しばらくお待ち下さい ")
                summary = Gpt().make_conversation_summary()
                Sql().store_conversation_summary(summary)
                Sql().store_conversation()
                beep.high()
                exit(1)
