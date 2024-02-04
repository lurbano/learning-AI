from transformers import AutoProcessor, BarkModel
import soundfile as sf
import time

# bark speaker library: https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
language = "ja"


processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

def speekPhrase(phrase, language="en", speakerNum=9):
    startTime = time.monotonic()
    voice_preset = f"v2/{language}_speaker_{i}"

    inputs = processor(phrase, voice_preset=voice_preset)

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    print (audio_array)
    sample_rate = model.generation_config.sample_rate

    sf.write(f"voiceTests/voiceTest_{language}_{i}.wav", audio_array, sample_rate)
    dt = time.monotonic() - startTime
    print(f"done {i} in {dt} sec.")


for i in range(10):
    speekPhrase("Welcome to the Makerspace! [laughs] Let's get to work.", language, i)


''' likes
en 8
en 9
es 6
fr 4
fr 5
de 7
de 3
de 2
it 6


'''