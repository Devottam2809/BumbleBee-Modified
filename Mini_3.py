import datetime
import pyttsx3
import speech_recognition as sr

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

            except Exception as error:
                return "none"

            return query.lower()

    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")

        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")

        else:
            self.speak("Good Evening!")

        # self.speak("I am Bumblebee Devottam. Please tell me how may I help you")
        self.speak("Hey DC, your assistant at your service")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.wish_me()
