import whisper

model = whisper.load_model("Models/vosk-model-small-uk-v3-small")
# result = model.transcribe("audio.mp3")
# print(result["text"])