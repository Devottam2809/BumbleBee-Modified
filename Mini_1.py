import pyttsx3
import speech_recognition as sr
import pvporcupine
import struct
import pyaudio
from winotify import Notification, audio
from Mini_3 import wishMe
from Mini_2 import start
from Mini_4 import taskxe

class VoiceAssistant:
    def __init__(self):
        self.assistant = pyttsx3.init('sapi5')
        voices = self.assistant.getProperty('voices')
        self.assistant.setProperty('voice', voices[1].id)
        self.assistant.setProperty('rate', 170)

    def speak(self, audio):
        print("  ")
        self.assistant.say(audio)
        print("  ")
        print(f" : {audio}")
        self.assistant.runAndWait()

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


class PorcupineAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()
        self.porcupine = None
        self.paud = None
        self.audio_stream = None

    def access(self):
        try:
            self.porcupine = pvporcupine.create(keywords=["bumblebee"])
            self.paud = pyaudio.PyAudio()
            self.audio_stream = self.paud.open(rate=self.porcupine.sample_rate, channels=1,
                                               format=pyaudio.paInt16, input=True,
                                               frames_per_buffer=self.porcupine.frame_length)
            while True:
                keyword = self.audio_stream.read(self.porcupine.frame_length)
                keyword = struct.unpack_from("h" * self.porcupine.frame_length, keyword)
                keyword_index = self.porcupine.process(keyword)
                if keyword_index >= 0:
                    start()
                    taskxe()

        finally:
            if self.porcupine is not None:
                self.porcupine.delete()
            if self.audio_stream is not None:
                self.audio_stream.close()
            if self.paud is not None:
                self.paud.terminate()


if __name__ == "__main__":
    voice_assistant = VoiceAssistant()
    porcupine_assistant = PorcupineAssistant()

    voice_assistant.speak("Initializing voice assistant")
    voice_assistant.speak("Checking for wake word")

    wishMe()  # Assuming wishMe is a part of Mini_3

    voice_assistant.speak("Initializing face recognition")
    voice_assistant.speak("Checking face match")

    porcupine_assistant.access()
