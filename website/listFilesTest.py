import glob

def listTranscriptFiles():
    path = "./audio/trans*.txt"
    dir_list = glob.glob(path)
    return sorted(dir_list, key=str.lower)

lastFile = listTranscriptFiles()[-1]
print("lastFile:", lastFile)

with open(lastFile, "r") as f:
    data = f.read()

print(data)