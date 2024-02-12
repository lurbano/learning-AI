# ref: https://huggingface.co/docs/transformers/en/chat_templating

from transformers import pipeline

gradeLevel = "high school student"
inputText = '''Geomagnetism is one of the oldest geophysical sciences. Geomagnetic fields have been observed and used since ancient times, and are still used for modern applications in navigation and mineral exploration. NCEI develops and distributes models of the geomagnetic field and maintains archives of geomagnetic data to further the understanding of Earth magnetism and the Sun-Earth environment.'''

# pipe = pipeline("conversational", "HuggingFaceH4/zephyr-7b-beta") #crashed
# pipe = pipeline("conversational", "mistralai/Mistral-7B-v0.1")    # large (may try again)
# pipe = pipeline("conversational", "microsoft/DialoGPT-small")       # no good answers
# pipe = pipeline("conversational", "microsoft/DialoGPT-large")       # no good answers
pipe = pipeline("conversational", "nomic-ai/gpt4all-j")       # no good answers
messages = [
    {
        "role": "system",
        "content": "You are a vocabulary assistant in a 9th grade classroom that returns a list of words and definitions.",
    },
    {"role": "user", "content": f"give me definitions of the words in the following passage that a typical {gradeLevel} would find difficult: {inputText}"},
]
print(pipe(messages))