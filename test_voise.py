import json, pyaudio
from vosk import Model, KaldiRecognizer
import open_file_linc as command
import time

model = Model("Models/vosk-model-small-uk-v3-small")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]
              
print("Я Слухаю ->>")
for text in listen():
    if text == "вихід":
        print("\nПака :)")
        quit()
        
    if text == "привіт":
        print("Здорова \nЯк справи?")
    
    if text == "відкрий музику":
        print("Відкриваю YouTube")
        # time.sleep(3)
        command.open_music()
    
    if text == "відкрий програму":
        print("Відкриваю QtDesigner")
        # time.sleep(3)
        command.open_file_Qt()
    
    if text == "ок":
        print("Хуйок \nхахахахаха")
        
        
    if text == "червоний":
        print("Red")
    
    if text == "зелений":
        print("Green")
    
    if text == "вимкнути":
        print("OFF")
    
    print(f"Команда ->>|{text}|<<- не роспізнана")
    

# command.open_music()
