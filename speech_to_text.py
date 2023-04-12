from abc import abstractmethod

import requests
import speech_recognition


class SpeechToText:

    @abstractmethod
    def speech_to_text(self, file_path, language):
        pass

class OpenAIWhisper(SpeechToText):

    def speech_to_text(self, file_path, language):
        with open(file_path, "rb") as f:
            response = requests.post(
                'https://api.openai.com/v1/audio/transcriptions',
                headers={
                    'Authorization': '' # TODO
                },
                files={
                    "file": (f.name, f),
                    'model': (None, 'whisper-1'),
                    'language': (None, language)
                }
            )
        return response.json()['text']


class SpeechRecognition(SpeechToText):

    recognizer = speech_recognition.Recognizer()
    lan_dict = {
        'zh': 'zh-CN'
    }

    def speech_to_text(self, file_path, language):
        audio_file = speech_recognition.AudioFile(file_path)


        with audio_file as source:
            audio_data = self.recognizer.record(source)

        text = self.recognizer.recognize_google(audio_data, language=self.lan_dict.get(language, language))
        return text




