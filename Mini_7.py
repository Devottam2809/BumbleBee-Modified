import pyttsx3
import speech_recognition as sr
import mysql.connector
from Mini_2 import push_notifications

class StudentDatabaseAssistant:
    def __init__(self):
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='psit123456789', database='finalproject')
        self.mycursor = self.mydb.cursor()
        self.Assistant = pyttsx3.init('sapi5')
        voices = self.Assistant.getProperty('voices')
        self.Assistant.setProperty('voice', voices[1].id)
        self.Assistant.setProperty('rate', 170)

    def speak(self, audio):
        print("  ")
        self.Assistant.say(audio)
        print("  ")
        print(f" : {audio}")
        self.Assistant.runAndWait()

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

    def execute_query_and_speak(self, query):
        push_notifications()
        self.mycursor.execute(query)
        for i in self.mycursor:
            self.speak(i)

    def names(self):
        self.execute_query_and_speak("select name from student")

    def feesubmit(self):
        self.execute_query_and_speak("select name from student where feesubmit='No'")

    def aname(self):
        self.execute_query_and_speak("select name from student where name like 'A%'")

    def dname(self):
        self.execute_query_and_speak("select name from student where name like 'D%'")

    def kname(self):
        self.execute_query_and_speak("select name from student where name like 'K%'")

    def sname(self):
        self.execute_query_and_speak("select name from student where name like 'S%'")

    def between_rollno(self):
        self.execute_query_and_speak("select name from student where rollno between 2101640100016 and 2101640100115")

if __name__ == "__main__":
    assistant = StudentDatabaseAssistant()
    assistant.names()
    # Uncomment and call other methods as needed
