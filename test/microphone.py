import sounddevice as sd

# 音声デバイスの一覧を取得
devices = sd.query_devices()

# 音声入力デバイスのみをフィルタリング
input_devices = [device for device in devices if device['max_input_channels'] > 0]

# 音声入力デバイスの一覧を出力
for device in input_devices:
    print(device)
