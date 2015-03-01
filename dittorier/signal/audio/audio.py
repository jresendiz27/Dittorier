__author__ = 'alberto'

from dittorier.config import SAMPLE_RATE, DURATION, CHANNELS, CHUNK, OUTPUT_AUDIO_FILENAME, logger, np
import pyaudio
import wave
from scipy.io.wavfile import read


def rec_audio(time=DURATION, rate=SAMPLE_RATE, filename=OUTPUT_AUDIO_FILENAME):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt8,
                    channels=CHANNELS,
                    rate=rate,
                    input=True,
                    frames_per_buffer=CHUNK)

    logger.debug("* recording")

    frames = []

    for i in range(0, int(rate / CHUNK * time)):
        data = stream.read(CHUNK)
        frames.append(data)

    logger.debug("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


def read_audio_file(name=OUTPUT_AUDIO_FILENAME):
    rate, data = read(name)
    data[np.abs(data) >= 20000] = 20000
    data[np.abs(data) <= 20] = 20
    return data