from abc import abstractmethod
import subprocess

class TextToSpeech:

    @abstractmethod
    def tts(self, text, language, speaker):
        pass

class AwsPolly(TextToSpeech):

    def tts(self, text, language, speaker):
        response = self.polly_client.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            # VoiceId='Joanna'  # Choose a voice, for example, 'Joanna' (US English)
            VoiceId=speaker
        )

        # Save the synthesized speech to an MP3 file
        output_file = "output.mp3"
        with open(output_file, 'wb') as f:
            f.write(response['AudioStream'].read())

        return output_file


class MacOSLocalTTS(TextToSpeech):

    def tts(self, text, language=None, speaker=None):
        if speaker:
            command = ['say', '-v', speaker, text]
        else:
            command = ['say', text]
        subprocess.run(command)
