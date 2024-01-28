import sounddevice as sd
import soundfile as sf
import numpy as np
import time

from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")



def fname(x):
    return f"{audioDir}rec{str(x).zfill(4)}.wav"

audioDir = "audio/"

sd.default.samplerate = fs = 44100

dt = 5.0  # seconds
ct = 0
# print(fname(5))

# for i in range(5):
#     filename = fname(i)

audioData = np.array([])


def callback(indata, frames, t, status):
    global ct
    global startTime
    global audioData
    if status:
        print(status, flush=True)


    audioData = np.append(audioData, indata)
    if ((time.monotonic() - startTime) >= dt):
        startTime = time.monotonic()
        # Save the audio data to a WAV file with a unique filename based on timestamp
        filename = fname(ct)
        ct += 1
        sf.write(filename, audioData, fs)
        x = transcriber(filename)
        print(x)
        #wavio.write(filename, indata[0], sample_rate, sampwidth=3)
        print(f"Audio saved to {filename}")
        audioData = np.array([])
        

# Set the sample rate and duration for recording
sample_rate = 44100  # You can adjust this value based on your requirements
duration = 20  # Recording duration in seconds (5 minutes)

print("Start...")
startTime = time.monotonic()
# Start recording using sounddevice
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))
