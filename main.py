from speech_to_text import SpeechRecognition
from text_to_speech import MacOSLocalTTS, AwsPolly, AzureTTS
from player import LocalPlayer
from ai_generator import OpenAI
from recorder import LocalRecorder
import argparse

local_recorder = LocalRecorder()
open_ai = OpenAI()
tts = MacOSLocalTTS()
player = LocalPlayer()
stt = SpeechRecognition()
azure_default_speaker = 'zh-CN-XiaoyouNeural'
aws_default_speaker = 'Joanna'

# prompt_prefix = "You are an English-speaking teacher helping a student practice their spoken English. Respond to the student's answer about the topic."
prompt_prefix = """
你是一个天真聪明小朋友，你喜欢陪小朋友聊天, 接下来和小朋友聊天吧, 
"""


def conversation_start(speaker):
    prompt = """
    %s

    小朋友: '{content}'
    """ % prompt_prefix
    reply = open_ai.generate(prompt_prefix, prompt)
    print("Teacher: " + reply)
    player.play_audio(tts.tts(reply, speaker=speaker))


def conversation_reply(speaker, language):
    file_path = local_recorder.record()
    text = stt.speech_to_text(file_path, language)

    print("小朋友: " + text)

    prompt = "%s\n%s" % (prompt_prefix, text)
    reply = open_ai.generate(prompt_prefix, prompt)
    print("Teacher: " + reply)
    player.play_audio(tts.tts(reply, speaker=speaker))


parser = argparse.ArgumentParser(description='Use voice to have a chat.')
parser.add_argument('--tts', type=str, help='select a tts service, 1. azure 2. aws 3. local')
parser.add_argument('--speaker', type=str, help='name of speaker')


if __name__ == '__main__':

    args = parser.parse_args()

    speaker = None
    language = 'zh'

    tts_op = args.tts
    if tts_op and tts_op == 'azure':
        tts = AzureTTS()
        speaker = azure_default_speaker
    elif tts_op and tts_op == 'aws':
        tts = AwsPolly()
        speaker = aws_default_speaker

    if args.speaker:
        speaker = args.speaker

    conversation_start(speaker)
    while True:
        conversation_reply(speaker, language)
