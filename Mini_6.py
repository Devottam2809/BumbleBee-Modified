import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.setProperty('rate', 170)

    def speak(self, audio):
        print("  ")
        self.engine.say(audio)
        print("  ")
        print(f" : {audio}")
        self.engine.runAndWait()

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

            try:
                print("Recognizing....")
                query = recognizer.recognize_google(audio, language='en-in')
                print(f"You said : {query}")

            except Exception as e1:
                return str(e1)

            return query.lower()

class LocationAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()

    def my_location(self):
        ip_address = requests.get('https://api.ipify.org').text
        url = f'https://get.geojs.io/v1/ip/geo/{ip_address}.json'
        geo_query = requests.get(url)
        geo_data = geo_query.json()
        state = geo_data['city']
        country = geo_data['country']
        self.speak(f"Sir, you are now in {state}, {country}")

class WeatherAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()

    def temperature(self):
        search = 'Temperature in kanpur'
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        self.speak(f"The temperature is: {temperature}")

class NotepadAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()

    def notepad(self):
        self.speak("I am ready to write")
        writes = self.take_command()
        self.speak("Do you want to save the file?")
        ask = self.take_command()

        if 'save' in ask:
            self.speak("Name the file...")
            time = self.take_command()
            filename = f"{time}_note.txt"
            with open(filename, "w") as file:
                file.write(writes)
            path1 = os.path.abspath(filename)
            os.startfile(path1)
            self.speak("File Saved...")
        else:
            self.speak("Draft Dumped")

if __name__ == "__main__":
    assistant = NotepadAssistant()
    assistant.notepad()
