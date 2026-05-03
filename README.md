# BrowserAssistant
simple voice‑controlled assistant that uses text‑to‑speech, speech‑to‑text, and browser automation to perform Google searches based on spoken commands.

The assistant generates a spoken greeting using PiperVoice.

It records the user’s response and transcribes it with Whisper.

If the user says “yes,” it asks what to search for.

The user speaks a search term.

The script transcribes the term and opens a Google search in the default browser.

Temporary audio files are cleaned up automatically.


Download the Lessac medium model:
https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
Place it in APIs/en_US-lessac-medium.onnx

dependencies: 
pyaudio
whisper
piper-tts
wave
winsound
torch
