from pydub import AudioSegment
from pydub.playback import play

class LocalPlayer:

    def play_audio(self, file_path):
        audio = AudioSegment.from_file(file_path)
        play(audio)

