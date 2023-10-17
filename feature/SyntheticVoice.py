import requests
import simpleaudio
import tempfile
import json

host = "127.0.0.1"  # "localhost"でも可能だが、処理が遅くなる
port = 50021


class SyntheticVoice:
    def __init__(self):
        self.host = host
        self.port = port

    def speaking(self, text):
        params = (
            ("text", text),
            ("speaker", 1)  # 音声の種類をInt型で指定
        )
        # 以下の検索結果でどの数値がどういった声なのか記載されている
        # https://github.com/VOICEVOX/voicevox_resource/search?q=styleId

        response1 = requests.post(
            f"http://{self.host}:{self.port}/audio_query",
            params=params
        )

        response2 = requests.post(
            f"http://{self.host}:{self.port}/synthesis",
            headers={"Content-Type": "application/json"},
            params=params,
            data=json.dumps(response1.json())
        )

        with tempfile.TemporaryDirectory() as tmp:
            with open(f"{tmp}/audi.wav", "wb") as f:
                f.write(response2.content)
                wav_obj = simpleaudio.WaveObject.from_wave_file(
                    f"{tmp}/audi.wav")
                play_obj = wav_obj.play()
                play_obj.wait_done()
