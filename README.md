# Voice-Chat-GPT
chat with ChatGPT(LLM) by VOICE on your laptop(MacOS)

## ENV
+ set up OpenAI key 
  ```bash
  # openAI 
  export  OPENAI_API_KEY=sk-xx
  # AWS
  export AWS_ACCESS_KEY=xxx
  export AWS_ACCESS_SECRET=xxx
  # Azure
  export AZURE_ACCESS_KEY=xxx
  export AZURE_ACCESS_REGION=xxx
  ```
+ install requirements
  ```
  // cd into the project dir, set up venv
  python -m venv venv
  . ./venv/bin/activate
  // install dependencies
  pip install -r requirements.txt
  ```

## RUN

```
python main.py -h
usage: main.py [-h] [--tts TTS] [--speaker SPEAKER]

Use voice to have a chat.

optional arguments:
  -h, --help         show this help message and exit
  --tts TTS          select a tts service, 1. azure 2. aws 3. local
  --speaker SPEAKER  name of speaker
```
```
# run
python main.py
python main.py --tts azure
```

