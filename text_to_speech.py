from abc import abstractmethod
import subprocess
import boto3
import azure.cognitiveservices.speech as speechsdk
import os


class TextToSpeech:

    @abstractmethod
    def tts(self, text, language, speaker):
        pass


class AwsPolly(TextToSpeech):
    aws_access_key = os.getenv('AWS_ACCESS_KEY')
    aws_access_secret = os.getenv('AWS_ACCESS_SECRET')

    polly_client = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
        region_name='us-east-1'
    ).client('polly')

    def tts(self, text, language=None, speaker='Joanna'):
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


class AzureTTS(TextToSpeech):
    access_key = os.getenv("AZURE_ACCESS_KEY")
    access_region = os.getenv("AZURE_ACCESS_REGION")

    speech_config = speechsdk.SpeechConfig(subscription=access_key, region=access_region)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    lang_speaker = {
        'zh': [
            'zh-CN-XiaoshuangNeural',
            'zh-CN-XiaoyouNeural',
            'zh-CN-XiaochenNeural',
            'zh-CN-XiaohanNeural',
            'zh-CN-XiaomengNeural',
            'zh-CN-XiaomoNeural',
            'zh-CN-XiaoqiuNeural',
            'zh-CN-XiaoruiNeural',
            'zh-CN-XiaoxiaoNeural',
            'zh-CN-XiaoxuanNeural',
            'zh-CN-XiaoyanNeural',
            'zh-CN-XiaoyiNeural',
            'zh-CN-XiaozhenNeural',
            'zh-CN-YunfengNeural',
            'zh-CN-YunhaoNeural',
            'zh-CN-YunjianNeural',
            'zh-CN-YunxiaNeural',
            'zh-CN-YunxiNeural',
            'zh-CN-YunyangNeural',
            'zh-CN-YunyeNeural',
            'zh-CN-YunzeNeural'
        ]
    }

    def tts(self, text, language=None, speaker='zh-CN-XiaoyouNeural'):
        self.speech_config.speech_synthesis_voice_name = speaker

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                         audio_config=self.audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")


class MacOSLocalTTS(TextToSpeech):

    def tts(self, text, language=None, speaker=None):
        if speaker:
            command = ['say', '-v', speaker, text]
        else:
            command = ['say', text]
        subprocess.run(command)
