import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText
import requests
import os
import webbrowser

from dotenv import load_dotenv

load_dotenv()


# 詳細情報を
def place_details(place_id):
    # ヘッダー情報
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],  # あなたのGoogle APIキー
        'X-Goog-FieldMask': 'googleMapsUri'  # websiteを取得するために指定
    }

    # GETリクエストを実行
    response = requests.get('https://places.googleapis.com/v1/places/{}'.format(place_id),
                            headers=headers)

    # レスポンスのJSONを取得
    data = response.json()
    # GoogleマップのURLを取得
    google_maps_url = data['googleMapsUri']

    return google_maps_url


def send_email(body):
    sendAddress = 'hexiliang04@gmail.com'
    password = os.environ['GOOGLE_APP_PWD']

    subject = 'MOWASからの案内です'
    bodyText = body
    fromAddress = 'hexiliang04@gmail.com'
    toAddress = 's20f1013@bene.fit.ac.jp'

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()
