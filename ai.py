import os
import json
import queue
import requests
import sounddevice as sd
from vosk import Model, KaldiRecognizer

VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3"

def speak(text):
    print("AI:",text)
    os.system(f'espeak-ng"{text}"')
