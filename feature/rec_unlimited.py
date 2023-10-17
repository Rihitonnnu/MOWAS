#!/usr/bin/env python3
"""Create a recording with arbitrary duration.

The soundfile module (https://python-soundfile.readthedocs.io/)
has to be installed!

"""
import speechRecognitionGoogle
import argparse
import tempfile
import queue
import sys
import datetime
import logging
import time as pf_time
import os
import beep

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

logger = logging.getLogger(__name__)
logger.setLevel(10)
sh = logging.StreamHandler()
logger.addHandler(sh)
fh = logging.FileHandler('../log/reaction/time_{}.log'.format(
    datetime.datetime.now().strftime('%Y%m%d_%H%M%S')), encoding='utf-8')
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

start = any
end = any

VOLUME_THRESHOLD = 10
IS_RECORDING = False

try:
    os.mkdir('../sound/{}'.format(datetime.datetime.now().strftime('%Y%m%d')))
except FileExistsError:
    pass


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())
    volume = numpy.linalg.norm(indata) * 10
    # logger.debug('volume power is {} '.format(volume))

    if volume > VOLUME_THRESHOLD:
        IS_RECORDING = True
        global end
        end = pf_time.perf_counter()


def recording_to_text():
    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])
        # if args.filename is None:
        args.filename = tempfile.mktemp(prefix=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
                                        suffix='.wav', dir='../sound/{}'.format(datetime.datetime.now().strftime('%Y%m%d')))

        beep.high()
        global start
        start = pf_time.perf_counter()
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                          channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                channels=args.channels, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
                    if pf_time.perf_counter()-start > 30:
                        raise Exception
    except KeyboardInterrupt:
        beep.low()
        print(end)
        print(start)
        logger.info('Reaction time is {}'.format(end-start))
        print('\nRecording finished: ' + repr(args.filename))
        text = speechRecognitionGoogle.speech_recognition(args.filename)
        return text
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))
