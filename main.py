import speech_recognition as sr
from speech_recognition import Recognizer
from thefuzz import fuzz, process
import subprocess
import webbrowser

ASSISTANT_NAMES = ['evolet','эволет', 'eva', 'эва', 'валет', 'evolu']
COMMANDS = ['включи', 'включить', 'включён', 'включен']
APPS = ['spotify', 'telegram', 'youtube']

r: Recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone(device_index=1) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)

            text = r.recognize_google(audio, language="ru-RU").lower()
            print(f"Recognized text: {text}")

            name_match, name_score = process.extractOne(text, ASSISTANT_NAMES, scorer=fuzz.partial_ratio)
            if name_score > 85:
                print(f"The bot's name is recognized: {name_match}")
                
                command_match, command_score = process.extractOne(text, COMMANDS, scorer=fuzz.partial_ratio)
                if command_score > 85:

                    print(f"The сommand is recognized: {command_match}")

                    app_match, app_score = process.extractOne(text, APPS, scorer=fuzz.partial_ratio)

                    if app_score > 85:
                        print(f"The app is recognized: {app_match}")
    
    except sr.UnknownValueError as e:
        pass
    except Exception as e:
        print(e)

