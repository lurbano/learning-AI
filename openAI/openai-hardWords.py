from openai import OpenAI
import json
import time
client = OpenAI()

gradeLevel = "high school student"
inputText = '''Geomagnetism is one of the oldest geophysical sciences. Geomagnetic fields have been observed and used since ancient times, and are still used for modern applications in navigation and mineral exploration. NCEI develops and distributes models of the geomagnetic field and maintains archives of geomagnetic data to further the understanding of Earth magnetism and the Sun-Earth environment.'''

print("Starting")
startTime = time.monotonic()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a vocabulary assistant in a 9th grade classroom that returns a list of words and definitions in JSON format."},
    {"role": "user", "content": f"give me definitions of the words in the following passage that a typical {gradeLevel} would find difficult: {inputText}"}
  ]
)
dt = time.monotonic() - startTime
print("Time taken:", dt)
print()

print(completion.choices[0].message)
print()
print(completion.choices[0].message.content)
print("type:", type(completion.choices[0].message.content))

print()
print("termList:")
termList = completion.choices[0].message.content
termList = json.loads(termList)
print("termList type:", type(termList))

print()
print(termList)

n = 0
for term, definition in termList.items():
    n+=1
    print(f"{n}: {term}: {definition}")






