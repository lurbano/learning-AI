from openai import OpenAI
import json
import time
client = OpenAI()
# ref:  https://cookbook.openai.com/examples/assistants_api_overview_python

def wait_on_run(run, thread):
    ct = 0
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
        ct += 0.5
        print (ct)
    return run

def show_json(obj):
    print(json.dumps(obj.model_dump_json(), indent=2))

# Pretty printing helper
def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()

def loadMessageJSON(messages):
    print("# Messages")
    m = messages[0]
    return json.loads(m.content[0].text.value)
    

gradeLevel = "high school student"
inputText = '''Geomagnetism is one of the oldest geophysical sciences. Geomagnetic fields have been observed and used since ancient times, and are still used for modern applications in navigation and mineral exploration. NCEI develops and distributes models of the geomagnetic field and maintains archives of geomagnetic data to further the understanding of Earth magnetism and the Sun-Earth environment.'''

assistant = client.beta.assistants.create(
    name="Hard Word Assistant",
    instructions=f"You are a vocabulary assistant to a {gradeLevel} that returns a list of words and definitions in JSON format.",
    model="gpt-3.5-turbo",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"give me definitions of the words in the following passage that a typical {gradeLevel} would find difficult: {inputText}",
)

print("Starting")
startTime = time.monotonic()

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

# Wait for completion
wait_on_run(run, thread)


dt = time.monotonic() - startTime
print("Time taken:", dt)
print()

# Retrieve all the messages added after our last user message
messages = client.beta.threads.messages.list(
    thread_id=thread.id, order="asc", after=message.id
)

pretty_print(messages)



# print(messages.data[0].content[0].value)
print()

termList = loadMessageJSON(messages)

n = 0
for term, definition in termList.items():
    n+=1
    print(f"{n}: {term}: {definition}")








