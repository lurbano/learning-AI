from transformers import AutoProcessor, BarkModel
import soundfile as sf

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

voice_preset = "v2/en_speaker_6"

inputs = processor("Welcome to the Makerspace! [laughs] Let's get to work.", voice_preset=voice_preset)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

print (audio_array)
sample_rate = model.generation_config.sample_rate

sf.write("voiceTest.wav", audio_array, sample_rate)