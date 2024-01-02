import pyaudio
import numpy as np

# 音声データの設定
CHUNK = 1024 * 2             # サンプル数
FORMAT = pyaudio.paInt16     # オーディオフォーマット
CHANNELS = 1                 # モノラル
RATE = 44100                 # サンプルレート

# PyAudioのインスタンスを生成
p = pyaudio.PyAudio()

# ストリームを開始
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

try:
    while True:
        # 音声データを読み込む
        data = stream.read(CHUNK)
        data_np = np.frombuffer(data, dtype='int16')

        # RMS値(データの二乗したものを平均して平方根を取る)を計算してデシベルに変換
        rms = np.sqrt(np.mean(data_np**2))
        db = 20 * np.log10(rms)

        # デシベル値を表示
        print("dB:", db)

except KeyboardInterrupt:
    # キーボード割り込みが発生した場合、ループを終了
    pass

finally:
    # ストリームとPyAudioのインスタンスを終了
    stream.stop_stream()
    stream.close()
    p.terminate()
