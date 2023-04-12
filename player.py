from pydub import AudioSegment
from pydub.playback import play

class LocalPlayer:

    def play_audio(self, file_path):
        if not file_path:
            return

        audio = AudioSegment.from_file(file_path)
        play(audio)

