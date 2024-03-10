import pyttsx3
import speech_recognition as sr
import speedtest
from winotify import Notification, audio

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 170)

    def speak(self, audio):
        print("  ")
        self.engine.say(audio)
        print("  ")
        print(f" : {audio}")
        self.engine.runAndWait()

class TaskExecutor:
    def __init__(self):
        self.voice_assistant = VoiceAssistant()

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

    def speed_test(self, query):
        self.voice_assistant.speak("Checking Speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correct_down = int(downloading / 800000)
        uploading = speed.upload()
        correct_upload = int(uploading / 800000)

        if 'upload speed' in query:
            self.voice_assistant.speak(f"The uploading speed is : {correct_upload} mbps")

        elif 'download speed' in query:
            self.voice_assistant.speak(f"The downloading speed is : {correct_down} mbps")

        else:
            self.voice_assistant.speak(f"The uploading speed is : {correct_upload} mbps and "
                                       f"the downloading speed is {correct_down} mbps")

class TaskExecutor:
    def __init__(self):
        self.voice_assistant = VoiceAssistant()
        self.notification_assistant = NotificationAssistant()

    def execute_task(self):
        query = self.voice_assistant.take_command()

        if 'hello' in query:
            speak("hello DC, just woke up")
            #speak("Ready for your service")
        
        elif 'go sleep' in query:
            speak("Bye Bye")
            #audio=AudioSegment.from_wav("NAintro.wav")
            #play(audio)
            #break 
        
        elif 'how are you' in query:
            speak("I am feeling A1")
            speak("And You ?")
        
        elif 'get lost' in query:
            speak("I am a virtual assistant , but you words are still very real")
            speak("please keep them respectful. ")

        elif 'thanks' in query:
            speak("It was the least I could do")

        elif 'thank you' in query:
            speak("It was the least I could do")

    #OS COMMAND
        elif 'restart' in query:
            speak("Comming back in a minute")
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            speak("bye bye !")
            os.system("shutdown /s /t 1")
        
        elif 'increase brightness' in query:
            #current_brightness = sbc.get_brightness()
            speak("The current brightness level is")
            speak(sbc.get_brightness())
            kk=sbc.get_brightness()
            #speak("What level of brightness do you want")
            #dd=takecommand()
            dd=kk[0]+40
            sbc.set_brightness(dd)
            speak("Brightness level set to")
            speak(dd)

        elif 'decrease brightness' in query:
            speak("The current brightness level is")
            speak(sbc.get_brightness())
            kk=sbc.get_brightness()
            #speak("What level of brightness do you want")
            #dd=takecommand()
            dd=kk[0]-40
            sbc.set_brightness(dd)
            speak("Brightness level set to")
            speak(dd)
        
    #Windows Automation
        elif 'Show desktop' in query:
            speak("Ok, switching to desktop")
            keyboard.press_and_release('windows + D')
        
        elif 'windows explorer' in query:
            speak("Ok, launching windows explorer")
            keyboard.press_and_release('windows + E')
        
        elif 'setting' in query:
            speak("launching windows settings")
            keyboard.press_and_release('windows + I')
        
        elif 'lock windows' in query:
            keyboard.press_and_release('windows + L')
            speak("Ok, locking the system")
            speak("I will take care of your data")

        elif 'run' in query:
            keyboard.press_and_release('windows + R')
            speak("What do you want to search ?")
            query=takecommand()
            keyboard.write(query)
            keyboard.press_and_release('enter')

        elif 'clipboard' in query:
            speak("Lets, see what you have collected")
            keyboard.press_and_release('windows + V')
        
        elif 'windows search' in query:
            keyboard.press_and_release('windows + Q')
            speak("What do you want to search ?")
            query=takecommand()
            keyboard.write(query)
            keyboard.press_and_release('enter')
    #Alarm
        elif 'set alarm' in query:
            speak("Enter the time :")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up Boss...")
                    from Mini_2 import startalarm
                    startalarm()
                    speak("Alarm Closed !")
                elif now>time:
                    break
        
        elif 'joke' in query:
            get  =pyjokes.get_joke()
            speak(get)
            from Mini_2 import laugh
            laugh()

        elif 'upload speed' in query:
            SpeedTest(query)
        
        elif 'download speed' in query:
            SpeedTest(query)
        
        elif 'internet speed' in query:
            SpeedTest(query)
        
        elif 'notepad' in query:
            from Mini_6 import notepad
            notepad()
        
        elif 'temperature' in query:
            from Mini_6 import temperature
            temperature()
        
        elif 'my location' in query:
            from Mini_6 import My_Location
            My_Location()
        
        elif 'screenshot' in query:
            kk=pyautogui.screenshot()
            speak('ok boss ! What should i name the file...')
            path = takecommand()
            path1name = path + ".png"
            path1 = "" + path1name
            kk.save(path1)
            speak('Snap captured')

        elif 'remember that' in query:
            remembermsg=query.replace('remember that',"")
            remembermsg=remembermsg.replace("bumblebee","")
            speak("You tell me to remind you that : "+remembermsg)
            remember = open('data.txt','w')
            remember.write(remembermsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            speak("You tell me that" + remember.read())
        
    #Chrome Automation
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Bumblebee","")
            query = query.replace("google search","")
            query = query .replace("google","")
            speak("This is what I found for your search...")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,1)
                speak(result)
            except:
                speak("No readable data")
        
        elif 'how to' in query:
            speak("Getting data from the internet...")
            op=query.replace("bumblebee","")
            result = 1
            howtofunc= search_wikihow(op,result)
            assert len(howtofunc)==1
            howtofunc[0].print()
            speak(howtofunc[0].summary)
        
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        
        elif 'anonymous' in query:
            keyboard.press_and_release('Ctrl + Shift + n')

        elif 'new tab' in query:
            keyboard.press_and_release('Ctrl + t')

        elif 'open previous tab' in query:
            keyboard.press_and_release('Ctrl + Shift + t')
        
        elif 'jump on next tab' in query:
            keyboard.press_and_release('Ctrl + Tab')
        
        elif 'jump on previous tab' in query:
            keyboard.press_and_release('Ctrl + Shift + Tab')

        elif 'close current tab' in query:
            keyboard.press_and_release('Ctrl + w')

        elif 'minimise' in query:
            keyboard.press('Alt')
            keyboard.press('Space')
            keyboard.press('n')
            keyboard.release('n')
            keyboard.release('Space')
            keyboard.release('Alt')

        #elif 'maximize' in query:
            #   keyboard.press_and_release('Alt + Space + X')
        
        elif 'close chrome' in query:
            keyboard.press_and_release('Alt + f4')
        
        elif 'clear browsing data' in query:
            keyboard.press_and_release('Ctrl + Shift + Delete')
        
        elif 'refresh the page' in query:
            keyboard.press_and_release('f5')
        
        elif 'print this page' in query:
            keyboard.press_and_release('Ctrl + p')
        
        elif 'save current page' in query:
            keyboard.press_and_release('Ctrl + s')

        elif 'bookmark' in query:
            keyboard.press_and_release('Ctrl + d')
            keyboard.press('enter')
        
        elif 'full screen' in query:
            keyboard.press_and_release('f11')
        
        elif 'close full screen' in query:
            keyboard.press_and_release('f11')
            
        elif 'zoomin' in query:
            keyboard.press('Ctrl')
            keyboard.press('+')
            keyboard.release('Ctrl')
            keyboard.release('+')
        
        #elif 'zoom out' in query:
            #   keyboard.press('Ctrl')
            #  keyboard.press('-')
            # keyboard.release('Ctrl')
            #keyboard.release('-')
        
        elif 'end of page' in query:
            keyboard.press_and_release('End')

        elif 'top of the page' in query:
            keyboard.press_and_release('Home')

        elif 'switch tab' in query:
            tab = query.replace("switch tab","")
            Tab = tab.replace("to","")
            num=Tab

            bb = f'Ctrl + {num}'
            keyboard.press_and_release(bb)

    #youtube automation
        elif 'youtube search'  in query:
            speak("OK Boss , This is what I found for your search !")
            query = query.replace("bumblebee","")
            query =query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir !")

        elif 'play' in query:
            keyboard.press_and_release('spacebar')

        elif 'pause' in query:
            keyboard.press_and_release('spacebar')

        elif 'mute' in query:
            keyboard.press_and_release('m')

        #elif 'forward' in query:
            #  keyboard.press_and_release('Right arrow')

        #elif 'backward' in query:
        #    keyboard.press_and_release('Left arrow')

        elif 'increase volume' in query:
            keyboard.press_and_release('Up Arrow')

        elif 'decrease volume' in query:
            keyboard.press_and_release('Down Arrow')

        elif 'fullscreen' in query:
            keyboard.press_and_release('f')

        elif 'caption' in query:
            keyboard.press_and_release('c')

        elif 'next video' in query:
            keyboard.press_and_release('Shift+N')

        elif 'past video' in query:
            keyboard.press_and_release("Shift+P")

        elif 'miniplayer' in query:
            keyboard.press_and_release("i")
        
        elif 'close youtube' in query:
            keyboard.press_and_release("alt+f4")

    #IOT Module
        elif 'turn on' in query or 'turn off' in query:
            from Mini_5 import IOT
            IOT(query)

    # SQL QUERIES
        elif 'get me names' in query:
            speak("Fetching records from the database")
            from Mini_7 import names
            names()
        
        elif 'give me' in query:
            speak("Fetching records from the database")
            #query = query.replace("bumblebee","")
            #query =query.replace("give me","")
            #query = query.replace("bumblebee","")
            #query =query.replace("list","")
            from Mini_7 import feesubmit
            feesubmit()
        
        elif 'name starts with' in query:
            speak("Fetching records from the database")
            from Mini_7 import kname
            kname()
        
        elif 'roll number' in query:
            speak("Fetching records from the database")
            # 16 to 115
            from Mini_7 import betweenrollno
            betweenrollno()
            
        elif 'time table' in query:
            from Mini_8 import time
            time()

            

if __name__ == "__main__":
    assistant = AssistantFunctions()
    assistant.show_notification()
    assistant.task_execution()

if __name__ == "__main__":
    task_executor = TaskExecutor()
    task_executor.notification_assistant.show_notification()
    task_executor.execute_task()
