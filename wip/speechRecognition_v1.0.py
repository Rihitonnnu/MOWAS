import concurrent.futures
import speech_recognition as sr
import beep as beep
import soundSurveillance
import time
import logging
import sounddevice as sd

# ログの設定
logging.basicConfig(filename='../log/pastTime.log',
                    filemode='w', level=logging.DEBUG)
logger = logging.getLogger()

audio = any


def audio_listen(r, source):
    global audio
    audio = r.listen(source)


def speech_recognition():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        beep.high()
        executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
        # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        executor.submit(soundSurveillance.SoundSurveillance())
        # start = time.perf_counter()
        # soundSurveillance.SoundSurveillance()
        executor.submit(audio_listen(r, source))
        # end = time.perf_counter()
        # audio_listen(r, source)
        # audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ja-JP')
        beep.low()
        print(text)
        # logger.debug(text)
        # logger.debug('Reaction time is {} seconds.'.format(end-start))
        return text

    except:
        beep.error()
        print("録音されていません")
        return None


# speech_recognition()
