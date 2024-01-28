== HuggingFace

Setup: https://huggingface.co/learn/nlp-course/chapter0/1
virtual environment (be in the folder you want for the project)
> python3 -m venv .env
> source .env/bin/activate

> pip install "transformers[sentencepiece]" 

pyTorch
Select the appropriate options on:
https://pytorch.org/get-started/locally/
> pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

default model:
https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english


webserver
> pip install aiohttp