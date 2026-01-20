mport os
import json
import queue
import requests
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# ----------------------------
# CONFIG
# ----------------------------
VOSK_MODEL_PATH = "/home/vijay/vosk-model-small-en-us-0.15"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3"

# ----------------------------
# SPEAK (TTS)
# ----------------------------
def speak(text):
    print("AI:", text)
    os.system(f'espeak-ng "{text}"')

# ----------------------------
# AI THINK (OLLAMA)
# ----------------------------
def ask_ai(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt
    }

    r = requests.post(OLLAMA_URL, json=payload, stream=True)
    return r.json()["response"]

    return reply.strip()


q = queue.Queue()

def audio_callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=audio_callback
    ):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result.get("text", "")

model = Model(VOSK_MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

speak("Voice assistant started. Say assistant to talk.")
while True:
    print("Listening...")
    text = listen()

    if text == "":
        continue

    print("You:", text)
    if "assistant" not in text:
        continue

    if "exit" in text or "bye" in text:
        speak("Goodbye")
        break

    reply = ask_ai(text)
    speak(reply)
