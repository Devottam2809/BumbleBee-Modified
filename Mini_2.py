from pydub import AudioSegment
from pydub.playback import play
from pushbullet import PushBullet

class AudioPlayer:
    def __init__(self):
        pass

    def play_audio(self, audio_path):
        audio = AudioSegment.from_wav(audio_path)
        play(audio)

class NotificationSender:
    def __init__(self, api_key):
        self.api_key = api_key

    def push_notification(self, title, message):
        pb = PushBullet(self.api_key)
        push = pb.push_note(title, message)

class SoundEffects:
    def __init__(self):
        pass

    def play_laugh(self):
        audio = AudioSegment.from_wav("laugh.wav")
        play(audio)

class AssistantManager:
    def __init__(self, api_key):
        self.audio_player = AudioPlayer()
        self.notification_sender = NotificationSender(api_key)
        self.sound_effects = SoundEffects()

    def start(self):
        self.audio_player.play_audio("startingaudio.wav")

    def start_alarm(self):
        self.audio_player.play_audio("alarmtone.wav")

    def push_notifications(self):
        file = "database.txt"
        with open(file, mode='r') as f:
            text = f.read()

        self.notification_sender.push_notification("Please Remember", text)

    def laugh(self):
        self.sound_effects.play_laugh()

if __name__ == "__main__":
    API_KEY = "o.Ny0v28aWyYe2HkbwMGZnWIJwtQmbhmdM"

    assistant_manager = AssistantManager(API_KEY)
    
    assistant_manager.push_notifications()  # Assuming you want to send notifications first
    assistant_manager.start()
    assistant_manager.start_alarm()
    assistant_manager.laugh()
