from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf

model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

text = "Welcome to the Makerspace! Let's get to work."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

print("output: ", output[0].float())

sf.write(f"voiceTests/voiceTest_Facebook.wav", output[0].float().numpy(), model.config.sampling_rate)
