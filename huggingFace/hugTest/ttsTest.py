from transformers import pipeline
import soundfile as sf

synthesizer = pipeline("text-to-speech", "suno/bark")

speech = synthesizer("Welcome to the Makerspace! [laughs] Let's get to work.")

print("Audio:", speech['audio'][0])
print("sample rate:", speech['sampling_rate'])
print()

sf.write("voiceTest.wav", speech["audio"][0], speech["sampling_rate"])