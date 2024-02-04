from transformers import AutoProcessor, BarkModel
import soundfile as sf

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
language = "es"

for i in range(10):
    voice_preset = f"v2/{language}_speaker_{i}"

    inputs = processor("Welcome to the Makerspace! [laughs] Let's get to work.", voice_preset=voice_preset)

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    print (audio_array)
    sample_rate = model.generation_config.sample_rate

    sf.write(f"voiceTest_{language}_{i}.wav", audio_array, sample_rate)
    print(f"done {i}")