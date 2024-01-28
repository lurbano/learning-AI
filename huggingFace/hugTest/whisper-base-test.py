from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

x = transcriber("recorded_audio.wav")

# classifier = pipeline("sentiment-analysis")
# x = classifier(
#     [
#         "I've been waiting for a HuggingFace course my whole life.",
#         "I hate this so much!",
#     ]
# )

print(x)
print("done")