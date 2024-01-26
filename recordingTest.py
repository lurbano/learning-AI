import sounddevice as sd
import soundfile as sf
import numpy as np

'''
Requires:
> pip install sounddevice numpy
> sudo apt install portaudio19-dev
'''


fs = 44100

duration = 5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
print('done')

# sd.play(myrecording, fs)
# print(myrecording)
# print('finished')

file_path = "recorded_audio.wav"  # Set the file path to save the recording
print(f"Saving recording to {file_path}...")
sf.write(file_path, myrecording, fs)
print("Recording saved.")