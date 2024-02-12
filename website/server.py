import asyncio
from aiohttp import web, ClientSession
from datetime import datetime
import json
from openai import OpenAI
from uAio import *

from uTranscribe import *
# set up transcriber
myTranscriber = uTranscribe()

async def handle(request):
    with open("index.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')

async def handlePost(request):
    data = await request.json()
    rData = {}
    # print(data)
    # print(data["action"], data["value"])

    if data['action'] == "getTime":
        now = datetime.now()
        print(now.ctime())
        rData['item'] = "time"
        rData['status'] = now.ctime() # a string representing the current time

    if data['action'] == 'photoResistor':
        # send request to the Makerspace picoW with the photoresistor
        info = await postRequest("20.1.0.96:80", action="photoResistor", value="")
        print("Requested from pr Pico: ", info)
        rData = json.loads(info)

    ''' Recording '''
    if data['action'] == "startRecording":
        print(datetime.now().ctime())
        myTranscriber.startRecording()
        rData['item'] = "startRecording"
        rData['status'] = datetime.now().ctime() # a string representing the current time

    if data['action'] == "stopRecording":
        print(datetime.now().ctime())
        await asyncio.sleep(5) # wait 5 seconds to stop recording
        myTranscriber.stopRecording()
        rData['item'] = "stopRecording"
        rData['status'] = datetime.now().ctime() # a string representing the current time

    if data['action'] == "lastCaption":
        #print("Last Caption")
        rData['item'] = "lastCaption"
        rData['status'] = myTranscriber.transcriptList[-1]

    if data['action'] == "getTranscript":
        #print("Full Transcript")
        rData['item'] = "getTranscript"
        rData['status'] = " <br> ".join(myTranscriber.transcriptList)

    if data['action'] == "hardWords":
        # hardWordsList = await getHardWords(data['value'])
        rData['item'] = "hardWords"
        rData['status'] = await getHardWords(data['value'])

    
    response = json.dumps(rData)
    # print("Response: ", response)
    return web.Response(text=response, content_type='text/html')


async def captionsPage(request):
    with open("captions.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')

async def hardWordsPage(request):
    with open("hardWords.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')



async def getHardWords(inputText, gradeLevel = "high school student"):
    print("OpenAI:", inputText)
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a vocabulary assistant in a 9th grade classroom that returns a list of words and definitions in JSON format."},
            {"role": "user", "content": f"give me definitions of the words in the following passage that a typical {gradeLevel} would find difficult: {inputText}"}
        ]
    )
    termList = completion.choices[0].message.content
    termListA = json.loads(termList)
    n = 0
    for term, definition in termListA.items():
        n+=1
        print(f"  {n}: {term}: {definition}")
    return termList


# print "Hello" every 1 second (testing async)
async def print_hello():
    while True:
        print("Hello")
        await asyncio.sleep(1)

''' Get the light level from the MakerspaceNetwork Testing Pico'''
async def getLightLevel(dt=1):
    while True:
        await getRequest('20.1.0.96:80/photoResistor')
        # async with ClientSession() as session:
        #     async with session.get('http://20.1.0.96:80/photoResistor') as resp:
        #         print(resp.status)
        #         print(await resp.text())
        await asyncio.sleep(dt)



async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post("/", handlePost)
    app.router.add_get("/captions", captionsPage)
    app.router.add_get("/hardWords", hardWordsPage)
    app.router.add_static('/static', 'static')
    
    runner = web.AppRunner(app)
    await runner.setup()

    host = getIP()
    site = web.TCPSite(runner, host, 8080)  # Bind to the local IP address
    await site.start()
    print(f"Server running at http://{host}:8080/")

    asyncio.create_task(print_hello())
    # asyncio.create_task(getLightLevel(dt=5))
    # asyncio.create_task(myTranscriber.findHardWords("This sentence"))

    '''Testing post request'''
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")

    await asyncio.Event().wait()  # Keep the event loop running

if __name__ == '__main__':
    asyncio.run(main())
