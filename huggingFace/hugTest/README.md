== HuggingFace

Setup: https://huggingface.co/learn/nlp-course/chapter0/1
virtual environment (be in the folder you want for the project)
```
python3 -m venv .env
source .env/bin/activate
pip3 install "transformers[sentencepiece]"
```


pyTorch
Select the appropriate options on:
https://pytorch.org/get-started/locally/

CPU only version (go to link above if you have CUDA or ROCm graphics cards)
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


## Gradio: easily build webpage for a model 
https://www.gradio.app/guides/quickstart

chatbot using langchain
https://www.gradio.app/guides/creating-a-chatbot-fast#a-langchain-example

## chat
Huggingface text-generation-interface:
https://github.com/huggingface/text-generation-inference


## Pipelines
https://huggingface.co/docs/transformers/v4.37.2/en/main_classes/pipelines#transformers.pipeline


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

* Testing bark voices use ttsTest4 and change the language (eg: language = "it" for italian) see:
    * Bark speakers: https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
```
python3 ttsTest4.py
```

* Transcribe from audio:
```bash
python3 transcribe2.py
```
or using the uTranscribe class test with:
```bash
python3 uTranscribe.py
```

## webserver
```
pip install aiohttp
```
