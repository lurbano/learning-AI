import os

def getTranscript():
    path = f"./audio/"
    txt_files = [f for f in os.listdir(path) if f.endswith(".txt")]
    transcript = ""
    for fname in sorted(txt_files, key=str.lower):
        with open(f"{path}{fname}") as f:
            transcript += f.read()
    # print (txt_files)
    # print(transcript)
    return transcript

if __name__ == "__main__":
    tscript = getTranscript()
    print(tscript)