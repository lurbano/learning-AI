import subprocess
import time

def sayText(toSay):
    subprocess.Popen(f'echo {toSay} | festival --tts', shell=True)
    time.sleep(4)

def saveTts(toSay, fname="output.wav"):
    subprocess.Popen(f'echo {toSay} | text2wave -o {fname}', shell=True)

sayText("Welcome to the Makerspace. Lets get to work.")
saveTts("Welcome to the Makerspace. Lets get to work.")