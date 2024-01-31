== HuggingFace

Setup: https://huggingface.co/learn/nlp-course/chapter0/1
virtual environment (be in the folder you want for the project)
```
python3 -m venv .env
source .env/bin/activate
pip install "transformers[sentencepiece]"
```


pyTorch
Select the appropriate options on:
https://pytorch.org/get-started/locally/
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

default model:
https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english


## Sound

install ffmpeg
```
sudo apt-get install ffmpeg libavcodec-extra
```

portaudio
```
sudo apt-get install libasound-dev
sudo apt-get install portaudio19-dev
```

sounddevice
```
pip install sounddevice numpy
pip install soundfile
```

* usage: https://python-sounddevice.readthedocs.io/en/latest/usage.html

Speech to Text
* Whisper: https://platform.openai.com/docs/guides/speech-to-text/quickstart


Text to Speech (in progress)

```
pip install git+https://github.com/suno-ai/bark.git
```

<!-- scipy
```
pip install scipy
``` -->

### Testing

* Record an audio clip (.wav) (5 sec):
```
python3 recordingTest.py
```
* Send to OpenAI Whisper to get transcript:
```
python3 whisperTest.py



## webserver
```
pip install aiohttp
```
