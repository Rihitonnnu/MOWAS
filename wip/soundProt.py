import pyaudio
import numpy
import matplotlib.pyplot as plot


def audiostart():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        rate=44100,
                        channels=1,
                        input_device_index=1,
                        input=True,
                        frames_per_buffer=1024)
    return audio, stream


def audiostop(audio, stream):
    stream.stop_stream()
    stream.close()
    audio.terminate()


def read_plot_data(stream):
    data = stream.read(1024)
    audiodata = numpy.frombuffer(data, dtype='int16')

    plot.plot(audiodata)
    plot.draw()
    plot.pause(0.001)
    plot.cla()


if __name__ == '__main__':
    (audio, stream) = audiostart()

    while True:
        try:
            read_plot_data(stream)
        except KeyboardInterrupt:
            break

    audiostop(audio, stream)
