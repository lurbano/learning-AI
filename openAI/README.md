# learning-OpenAI

## OpenAI
* Quickstart
** https://platform.openai.com/docs/quickstart?context=python

virtual environment
> python -m venv openai-env
> source openai-env/bin/activate

openai
> pip install --upgrade openai

get API key (you have to put money on the account to get it to work, it seems)


## Sound

install ffmpeg
> apt-get install ffmpeg libavcodec-extra

portaudio
> sudo apt-get install libasound-dev
> sudo apt-get install portaudio19-dev


sounddevice
> pip install sounddevice numpy
> pip install soundfile

* usage: https://python-sounddevice.readthedocs.io/en/latest/usage.html

Speech to Text
* Whisper: https://platform.openai.com/docs/guides/speech-to-text/quickstart

## Testing

* Record an audio clip (.wav) (5 sec):
** > python3 recordingTest.py
* Send to OpenAI Whisper to get transcript:
** > python3 whisperTest.py
