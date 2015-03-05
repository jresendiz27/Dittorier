__author__ = 'alberto'

from dittorier.config import SAMPLE_RATE, DURATION, CHANNELS, CHUNK, OUTPUT_AUDIO_FILENAME, CHROMOSOME_LENGTH, logger, \
    np, MAX_FREQUENCY, MIN_FREQUENCY
import pyaudio
import wave
from scipy.io.wavfile import read, write


def rec_audio(time=DURATION, rate=SAMPLE_RATE, filename=OUTPUT_AUDIO_FILENAME):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt8,
                    channels=CHANNELS,
                    rate=rate,
                    input=True,
                    frames_per_buffer=CHUNK)

    logger.debug("recording")

    frames = []

    for i in range(0, int(rate / CHUNK * time)):
        data = stream.read(CHUNK)
        # Cleaning data
        data[np.abs(data) >= MAX_FREQUENCY] = MAX_FREQUENCY
        data[np.abs(data) <= MIN_FREQUENCY] = MIN_FREQUENCY
        frames.append(data)

    logger.debug("done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    return True


def read_audio_file(name=OUTPUT_AUDIO_FILENAME):
    rate, data = read(name)
    data[np.abs(data) >= MAX_FREQUENCY] = MAX_FREQUENCY
    data[np.abs(data) <= MIN_FREQUENCY] = MIN_FREQUENCY
    data = data.tolist()
    # Removing some samples to force the signal to fit into specific chunk size without resizing
    while not len(data) % CHROMOSOME_LENGTH == 0:
        data.pop()

    return data


def write_audio_file(name=OUTPUT_AUDIO_FILENAME, data=[]):
    local_data = np.asarray(data,dtype='int16')
    write(name, 2000, local_data)
    return True