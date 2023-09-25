import speech_recognition as sr
import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)
sh = logging.StreamHandler()
logger.addHandler(sh)
fh = logging.FileHandler('../log/userSpeech.log', encoding='utf-8')
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)


def speech_recognition(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    speechText = r.recognize_google(audio, language='ja-JP')
    print(speechText)
    logger.info(speechText)
    return speechText
