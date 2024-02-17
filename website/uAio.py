import subprocess
from aiohttp import ClientSession
import json

''' Get IP address (on Linux type devices)'''
def getIP():
    try:
        cmd = f'hostname -I'
        result = subprocess.run(cmd, shell = True, 
                                capture_output=True, text=True)
        # print(cmd)
        # print(result.stdout)
        ip = result.stdout.split(" ")
        return ip[0]
    except:
        print("Unable to find IP address. Reverting to localhost.")
        return "localhost"

''' Generic GET request '''
async def getRequest(addr="20.1.0.96:80/photoResistor"):
    url = f'http://{addr}'
    async with ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text()
            if l_print:
                print(resp.status)
                print("Pico (GET) response:", data)
            return data

''' send POST request to another MakerspaceNetwork device '''
async def postRequest(addr="192.168.1.142:8000", action="", value="", l_print=False):
    data = {}
    data["action"] = action
    data["value"] = value
    url = f'http://{addr}'
    async with ClientSession() as session:
        async with session.post(url, data=json.dumps(data)) as resp:
            # print(await resp.text())
            data = await resp.text()
            if l_print:
                print(resp.status)
                print("Pico (POST) response:", data)
            return data