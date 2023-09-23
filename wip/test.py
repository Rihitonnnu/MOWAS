import sounddevice as sd
import wave


fs = 48000

FILE_NAME = '../sound/test.wav'  # 保存するファイル名

duration = 5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

with wave.open(FILE_NAME, mode='wb') as wb:
    wb.setnchannels(1)  # モノラル
    wb.setsampwidth(2)  # 16bit=2byte
    wb.setframerate(fs)
    wb.writeframes(myrecording.tobytes())  # バイト列に変換
