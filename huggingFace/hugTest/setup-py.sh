#!/bin/bash

python3 -m venv .env
source .env/bin/activate
pip install "transformers[sentencepiece]"
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7
pip install sounddevice numpy
pip install soundfile