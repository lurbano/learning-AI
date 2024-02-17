import sounddevice as sd
import soundfile as sf
import numpy as np
import time
from transformers import pipeline
import subprocess
import asyncio
import glob
from openai import OpenAI
import json

class uTranscribe:

    def __init__(self):
        
        self.transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

        # Set the sample rate and duration for recording
        sd.default.samplerate = fs = 44100
        self.samplerate = 44100
        self.duration = 15  # Recording duration in seconds (5 minutes)

        self.dt = 5.0  # length of each clip in seconds
        
        self.audioDir = "audio/"
        self.audioData = np.array([])

        self.transcript = ''
        self.lastTranscriptFile = ""
        self.transcriptList = ["Initial"]
        self.transcriptListLength = len(self.transcriptList)

        self.hardWordsString = ""
        self.hardWords = []
        self.hardWordsDict = {}
        self.hardWordsTasks = []
        

        self.stream = sd.InputStream(callback=self.callback, channels=1)

    def printHardsWordsDict(self):
        n = 0
        for term, definition in self.hardWordsDict.items():
            n += 1
            print(f"  {n}: {term}: {definition}")

    def fname(self, n, kind="rec"):
        if kind == "rec":
            prefix = "rec"
            ftype = "wav"
        else:
            prefix = kind
            ftype = "txt"
        return f"{self.audioDir}{prefix}{str(n).zfill(4)}.{ftype}"

    def writeFinalTranscript(self):
        with open(f"{self.audioDir}finalTranscript.txt", "w") as f:
            f.write(self.transcript)


    def callback(self, indata, frames, t, status):

        if status:
            print(status, flush=True)


        self.audioData = np.append(self.audioData, indata)
        if ((time.monotonic() - self.startTime) >= self.dt):
            self.startTime = time.monotonic()
            # Save the audio data to a WAV file with a unique filename based on timestamp
            filename = self.fname(self.ct)
            self.ct += 1
            sf.write(filename, self.audioData, self.samplerate)
            x = self.transcriber(filename)
            print(x)
            tfileName = self.fname(self.ct, "trans")
            with open(tfileName, "w") as f:
                f.write(x['text'])
            self.lastTranscriptFile = tfileName
            self.transcriptList.append(x['text'])
            self.transcript += x['text']
            asyncio.run(self.checkHardWords(x['text']))
            # self.hardWordsTasks.append(asyncio.create_task(self.checkHardWords(x['text'])))
            #wavio.write(filename, indata[0], sample_rate, sampwidth=3)
            print(f"Audio saved to {filename}")
            self.audioData = np.array([])
        
    def startDuration(self):
        print("Start...")
        self.startTime = time.monotonic()
        # Start recording using sounddevice
        with sd.InputStream(callback=self.callback, channels=1):
            #sd.sleep(int(self.duration * 1000))
            time.sleep(self.duration)
            self.stop()

    def startKeyboard(self):
        print("Start...")
        self.startTime = time.monotonic()
        with sd.InputStream(callback=self.callback, channels=1):
            k = input("Press Enter to stop... ")
            self.stop()

    def stop(self):
        sd.stop()
        self.writeFinalTranscript()
        print("Done")
        print(self.transcript)
        return(self.transcript)

        
    def startRecording(self):
        self.ct = 0     # keep track of each recording
        self.transcriptList = ["Starting"]    #empty transcript list

        # empty audio folder
        cmd = f'rm ./{self.audioDir}trans*.txt ./{self.audioDir}rec*.wav'
        subprocess.run(cmd, shell = True)

        print("Start recording ...")
        self.startTime = time.monotonic()
        self.stream.start()

    def stopRecording(self):
        self.stream.stop()
        print("Done")
        print("Transcript: ", self.transcript)
        self.writeFinalTranscript()
        return self.transcript


    async def checkHardWords(self, txt):
        nHardWordsList = 0
        checkTxt = ""
        # txt = self.transcriptList[-1].strip()
        if txt != "Initial" and txt != "Starting":
            nHardWordsList = len(self.transcriptList)
            print("New Text:", self.transcriptList[-1])
            ''' Check to see if we need to find hard words'''
            tmpTxt = "" + txt
            checkTxt += txt
            
            if hasLongWords(txt, 5):
                print("  Has Long Words")
                hardW = await self.getHardWords(checkTxt)
                print()
                print("Hard Words Dictionary")
                self.printHardsWordsDict()
                print()
                
                checkTxt = ""
            else:
                print("  No Long Words")
                    
    async def getHardWords(self, inputText, gradeLevel = "undergraduate", courseType="scientific"):
        print("Sending to OpenAI:", inputText)
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a note-taking assistant to a {gradeLevel} student that only returns a list of {courseType} terms, with their definitions in word:definition JSON format."},
                {"role": "user", "content": f"give me definitions of the {courseType} words in the following passage that a {gradeLevel} student would find difficult: {inputText}"}
            ]
        )
        try:
            termList = completion.choices[0].message.content
            print()
            print("TermList")
            print(termList)
            print()
            termListA = json.loads(termList)
            n = 0
            for term, definition in termListA.items():
                n+=1
                print(f"  {n}: {term}: {definition}")
                if not term in self.hardWordsDict:
                    self.hardWordsDict[term] = definition
            return termList
        except:
            return {}




    def listTranscriptFiles(self):
        path = f"./{self.audioDir}trans*.txt"
        print("path: ", path)
        dir_list = glob.glob(path)
        return sorted(dir_list, key=str.lower)

    def lastTranscriptFile(self):
        print("getting last transcript file")
        return self.listTranscriptFiles()[-1]


    def getLastCaption(self):
        if self.lastTranscriptFile == "":
            return ""
        try: 
            with open(self.lastTranscriptFile, "r") as f:
                data = f.read()
            print(data)
            return data
        except:
            print("No file")
            return ""
    
def hasLongWords(txt, maxLength=5):
    for word in txt.split():
        if len(word) > maxLength:
            return True
    return False

if __name__ == "__main__":
    myTranscriber = uTranscribe()
    myTranscriber.startRecording()
    time.sleep(15)
    myTranscriber.stopRecording()

    