import sounddevice as sd
import numpy as np
import beep as beep
import logging
import logging.handlers
import time as pf_time
import wave
import datetime
import time
import os

import speechRecognitionGoogle
import log

# 1回音がなってから音が無になる時間が長時間続いた場合に録音を終了する

# ログの設定
logger = log.Log('../log/soundSurveillance.log').setup()


# 開始と終了時間
start = any
end = any

try:
    os.mkdir('../sound/{}'.format(datetime.datetime.now().strftime('%Y%m%d')))
except FileExistsError:
    pass

# 保存するファイル名
FILE_NAME = '../sound/{}/test_{}.wav'.format(datetime.datetime.now().strftime('%Y%m%d'),
                                             datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
wave_length = 10  # 録音する長さ（秒）
sample_rate = 16_000  # サンプリング周波数

# 音声データ
data = any


class SpeechRecognition:
    DURATION = 1
    STANDBYTIME = 30
    VOLUME_THRESHOLD = 30
    recording = False

    def __init__(self):
        self.listen_sound()

    def listen_sound(self):
        global data
        duration = 20  # 音声チェックを一時的に続ける秒数
        recordingStart = pf_time.perf_counter()
        while not self.recording and not pf_time.perf_counter()-recordingStart > self.STANDBYTIME:
            with sd.InputStream(callback=self.detect_sound):
                beep.high()
                time.sleep(0.4)
                global start
                start = pf_time.perf_counter()
                data = sd.rec(int(wave_length * sample_rate),
                              sample_rate, channels=1)
                sd.sleep(duration * 1000)
        if self.recording == False:
            self.is_not_confirmed_voice()

    def detect_sound(self, indata, frames, time, status):
        if self.recording == False:
            volume = np.linalg.norm(indata) * 10
            # logger.debug('volume power is {} '.format(volume))

            if volume > self.VOLUME_THRESHOLD:
                self.recording = True
                global end
                end = pf_time.perf_counter()
                self.finish_sound_detect()

    def is_not_confirmed_voice(self):
        print('音声が一定時間内に確認されませんでした')
        exit(1)

    # 音検知を終えて録音したデータの処理を行う
    def finish_sound_detect(self):

        logger.debug('Reaction time is {}'.format(end-start))
        beep.low()
        sd.wait()
        # ノーマライズ。量子化ビット16bitで録音するので int16 の範囲で最大化する
        global data
        data = data / data.max() * np.iinfo(np.int16).max

        # float -> int
        data = data.astype(np.int16)

        # ファイル保存
        with wave.open(FILE_NAME, mode='wb') as wb:
            wb.setnchannels(1)  # モノラル
            wb.setsampwidth(2)  # 16bit=2byte
            wb.setframerate(sample_rate)
            wb.writeframes(data.tobytes())  # バイト列に変換

        speechRecognitionGoogle.speech_recognition(FILE_NAME)
