import pyttsx3
import speech_recognition as sr
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
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing....")
                query = command.recognize_google(audio, language='en-in')
                print(f"You said : {query}")

            except Exception as Error:
                return "none"

            return query.lower()

class DailyRoutineAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()

    def time(self):
        hour = int(datetime.now().strftime("%H"))
        if 6 < hour <= 7:
            self.speak('In this time, you have to workout.')

        elif 9 <= hour <= 12:
            self.speak("In this time you have to study Maths, because the CT marks are just disgusting.")

        elif 16 <= hour <= 18:
            self.speak("Time to code. Make a post on Github. Check your LinkedIn.")

        elif 20 <= hour <= 25:
            self.speak("In this time you have to study.")
        else:
            self.speak("Take Rest")

if __name__ == "__main__":
    assistant = DailyRoutineAssistant()
    assistant.time()
