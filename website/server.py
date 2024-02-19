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
        print("startRecording: doHardWords", data["value"]["doHardWords"])
        print("Start Recording:", datetime.now().ctime())
        # setup for hard words or not
        myTranscriber.doHardWords = data["value"]["doHardWords"]
        # start recording
        myTranscriber.startRecording()
        # return info
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
        # rData['status'] = await getHardWords(data['value'])
        rData['status'] = myTranscriber.hardWordsDict

    if data['action'] == "nHardWords":
        # hardWordsList = await getHardWords(data['value'])
        rData['item'] = "nHardWords"
        # rData['status'] = await getHardWords(data['value'])
        rData['status'] = len(myTranscriber.hardWordsDict)

    if data['action'] == "dialPercent":
        try:
            id = data["value"]
            val = await postRequest(addr=f"20.1.0.{id}", action="dialPercent")
            val = json.loads(val)
            rData['item'] = "dialPercent"
            rData['status'] = val["status"]
        except:
            rData['item'] = "dialPercent"
            rData['status'] = "None"

    if data['action'] == "getDialPercent":
        try:
            id = data["value"]
            val = await postRequest(addr=f"20.1.0.{id}", action="dialPercent")
            val = json.loads(val)
            rData['item'] = data['action']
            rData['status'] = val["status"]
        except:
            rData['item'] = data['action']
            rData['status'] = "None"


    if data['action'] == "getLightLevel":
        try:
            id = data["value"]
            val = await getLightLevel()
            rData['item'] = "getLightLevel"
            rData['status'] = val
        except:
            rData['item'] = data['action']
            rData['status'] = "None"

     
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

async def studentPage(request):
    with open("student.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')



# print "Hello" every 1 second (testing async)
async def print_hello():
    while True:
        print("Hello")
        await asyncio.sleep(1)

''' Get the light level (defaults to the MakerspaceNetwork Testing Pico)'''
async def getLightLevel(addr='20.1.0.96:80'):
    try:
        data = await postRequest(addr=f"{addr}", action="photoResistor")
        data = json.loads(data)
        return data['status']
    except:
        return "None"


async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post("/", handlePost)
    app.router.add_get("/captions", captionsPage)
    app.router.add_get("/hardWords", hardWordsPage)
    app.router.add_get("/student", studentPage)
    # app.router.add_static('/static', 'static')
    
    runner = web.AppRunner(app)
    await runner.setup()

    host = getIP()
    site = web.TCPSite(runner, host, 8080)  # Bind to the local IP address
    await site.start()
    print(f"Server running at http://{host}:8080/")

    lightLevel = await getLightLevel()
    print("Light Level: ", lightLevel)

    # asyncio.create_task(print_hello())
    '''    '''
    # asyncio.create_task(checkHardWords())


    # asyncio.create_task(getLightLevel(dt=5))
    # asyncio.create_task(myTranscriber.findHardWords("This sentence"))

    '''Testing post request'''
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")

    await asyncio.Event().wait()  # Keep the event loop running

if __name__ == '__main__':
    asyncio.run(main())
