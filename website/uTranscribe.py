import sounddevice as sd
import soundfile as sf
import numpy as np
import time
from transformers import pipeline

class uTranscribe:

    def __init__(self):
        
        self.transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-base")

        # Set the sample rate and duration for recording
        sd.default.samplerate = fs = 44100
        self.samplerate = 44100
        self.duration = 15  # Recording duration in seconds (5 minutes)

        self.dt = 5.0  # length of each clip in seconds
        self.ct = 0     # keep track of each recording

        self.audioDir = "audio/"
        self.audioData = np.array([])

        self.transcript = ''

        self.stream = sd.InputStream(callback=self.callback, channels=1)


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
        # global ct
        # global startTime
        # global audioData
        # global transcript
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
            with open(self.fname(self.ct, "trans"), "w") as f:
                f.write(x['text'])
            self.transcript += x['text']
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
        print("Start recording ...")
        self.startTime = time.monotonic()
        self.stream.start()

    def stopRecording(self):
        self.stream.stop()
        print("Done")
        print("Transcript: ", self.transcript)
        return self.transcript

    

if __name__ == "__main__":
    myTranscriber = uTranscribe()
    myTranscriber.startRecording()
    time.sleep(15)
    myTranscriber.stopRecording()

    