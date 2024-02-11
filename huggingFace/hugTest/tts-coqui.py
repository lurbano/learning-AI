# https://github.com/coqui-ai/TTS
import subprocess


def sayTextCoqui(toSay):
    subprocess.Popen(f'tts --text "{toSay}" --out_path voiceTests/voiceTest-coqui.wav', shell=True)


sayTextCoqui("Welcome to the Makerspace. Lets get to work")