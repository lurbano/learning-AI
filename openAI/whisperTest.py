from openai import OpenAI
client = OpenAI()

audio_file= open("recorded_audio.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

# with open("output.txt", "w") as f:
#     f.write(transcript)

print(transcript)