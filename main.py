from speech_to_text import SpeechRecognition
from text_to_speech import MacOSLocalTTS
from player import LocalPlayer
from ai_generator import OpenAI
from recorder import LocalRecorder

local_recorder = LocalRecorder()
open_ai = OpenAI()
tts = MacOSLocalTTS()
player = LocalPlayer()
stt = SpeechRecognition()

prompt_prefix = "You are an English-speaking teacher helping a student practice their spoken English. Respond to the student's answer about the topic."

def conversation_start():
    prompt = """
    %s

    Student: I like the topic of buying things in a mall.
    """ % prompt_prefix
    reply = open_ai.generate(prompt_prefix, prompt)
    print("Teacher: " + reply)
    player.play_audio(tts.tts(reply))

def conversation_reply():
    file_path = local_recorder.record()
    text = stt.speech_to_text(file_path, 'en')

    print("Student: " + text)

    prompt = "%s\n%s" % (prompt_prefix, text)
    reply = open_ai.generate(prompt_prefix, prompt)
    print("Teacher: " + reply)
    player.play_audio(tts.tts(reply))


if __name__ == '__main__':
    conversation_start()
    while True:
        conversation_reply()