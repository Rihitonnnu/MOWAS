import sounddevice as sd
import numpy as np
import beep as beep
import logging
import time as pf_time

# ログの設定
logging.basicConfig(filename='../log/soundSurveillance.log',
                    filemode='w', level=logging.DEBUG)
logger = logging.getLogger()

# 開始と終了時間
start = any
end = any


class SoundSurveillance:
    DURATION = 1
    VOLUME_THRESHOLD = 10
    recording = False

    def __init__(self):
        self.listen_sound()

    def listen_sound(self):
        global start
        start = pf_time.perf_counter()
        duration = 5  # 音声チェックを一時的に続ける秒数
        while not self.recording:
            with sd.InputStream(callback=self.detect_sound):
                sd.sleep(duration * 1000)

    def detect_sound(self, indata, frames, time, status):
        if self.recording == False:
            volume = np.linalg.norm(indata) * 10
            logger.debug('volume power is {} '.format(volume))
            if volume > self.VOLUME_THRESHOLD:
                self.recording = True
                global end
                end = pf_time.perf_counter()
                self.finish_sound_detect()

    def finish_sound_detect(self):
        logger.debug('Reaction time is {}'.format(end-start))
        beep.high()
