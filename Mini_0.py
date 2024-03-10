import struct
import pyaudio
from winotify import Notification, audio
from urllib.request import urlopen

import face_recognition
import cv2
import numpy as np

import pyttsx3
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self):
        self.assistant = pyttsx3.init("sapi5")
        voices = self.assistant.getProperty("voices")
        self.assistant.setProperty("voice", voices[1].id)
        self.assistant.setProperty("rate", 170)

        self.toast = Notification(
            app_id="BumbleBee Launched",
            title="Voice Assistant Activated",
            msg="Hi! I am BumbleBee, your Multipurpose Voice Assistant.",
            duration="short",
            icon="D:\All codes\Mini_Function\Mini Function OOPS\Bumblebeeicon.png",
        )
        self.toast.set_audio(audio.Default, loop=False)
        self.toast.add_actions(
            label="Click Here", launch="C:/Users/91745/Desktop/Final Finished Code"
        )

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
                query = command.recognize_google(audio, language="en-in")
                print(f"You said : {query}")

            except Exception as Error:
                return "none"

            return query.lower()


class FaceRecognitionAssistant(VoiceAssistant):
    def __init__(self):
        super().__init__()
        self.video = cv2.VideoCapture(0)
        self.face_encoding_list = [face_recognition.face_encodings(face_recognition.load_image_file("image.jpg"))[0]]
        self.s = True

    def check_internet(self):
        try:
            urlopen("https://www.google.com", timeout=1)
            return True
        except:
            return False

    def start_animation(self):
        # Add your animation logic here
        pass

    def main_program(self):
        # Add your main program logic here
        pass

    def face_recognition_process(self):
        speak("initializing face recognition")
        speak("checking for a match")

        video = cv2.VideoCapture(0)

        face = face_recognition.load_image_file("image.jpg")
        faceencoding = face_recognition.face_encodings(face)[0]

        face_encodings_list = [faceencoding]

        face_encodings = []
        s = True
        face_coordinates = []

        while True:
            _, frame = self.video.read()
            resized_frame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)
            resized_frame_rgb = resized_frame[:, :, ::-1]

            if self.s:
                face_coordinates = face_recognition.face_locations(resized_frame_rgb)
                face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)

                for faces in face_encodings:
                    matches = face_recognition.compare_faces(self.face_encoding_list, faces)
                    if matches[0] == True:
                        self.video.release()
                        cv2.destroyAllWindows()
                        self.speak("Access Granted")
                        self.speak("Initializing...")
                        self.speak("Checking all ports and connections...")
                        self.speak("Checking Internet connection...")
                        if self.check_internet():
                            self.speak("  ")
                            self.speak("You are now Online !")
                            
                            self.start_animation()
                            self.toast.show()
                            print("hotword detected")
                            self.main_program()
                        else:
                            self.speak("No Internet Connection")
            else:
                self.speak("Access denied")
                break

if __name__ == "__main__":
    face_recognition_assistant = FaceRecognitionAssistant()
    face_recognition_assistant.face_recognition_process()
