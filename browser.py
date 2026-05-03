import webbrowser
import whisper
import wave
import os
from piper import PiperVoice
import winsound
from AudioRecordTranscribe import K_AudioRecord
from AudioRecordTranscribe import Transcribe


voice = PiperVoice.load("APIs/en_US-lessac-medium.onnx")
with wave.open("test.wav", "wb") as wav_file:
    voice.synthesize_wav("Hello, would you like to search something on the web?", wav_file)
winsound.PlaySound("test.wav", winsound.SND_FILENAME)
os.remove("test.wav")
K_AudioRecord()
search = Transcribe("output.wav")
if "yes" in search.lower():
    with wave.open("test.wav", "wb") as wav_file:
        voice.synthesize_wav("What would you like to search for?", wav_file)
    winsound.PlaySound("test.wav", winsound.SND_FILENAME)
    K_AudioRecord()
    term = Transcribe("output.wav")
    webbrowser.open(f'https://www.google.com/search?q={term}')
    

os.remove("output.wav")