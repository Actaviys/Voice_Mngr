# В командний рядок-> python -m speech_recognition

import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    # query = sr.recognize_google_cloud(audio_data=audio, language='uk-UA').lower()
    query = sr.recognize_google(audio_data=audio).lower()


print(query)
