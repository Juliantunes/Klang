#main.py

import pyaudio
import wave
import numpy as np
import scipy.fft





audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

#concatenate frames into single byte string
raw_data = b''.join(frames)

format = pyaudio.paInt16
x = np.frombuffer(raw_data, dtype=np.int16)
y = scipy.fft(x)

yinv = scipy.fft.ifft(y)




# Use wave module to write the frames to a WAV file
with wave.open("myrecording.wav", "wb") as sound_file:
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))

