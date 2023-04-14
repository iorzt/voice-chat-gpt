import pyaudio
import wave

class LocalRecorder:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10 # record duration
    OUTPUT_FILE = "output.wav"

    audio = pyaudio.PyAudio()


    def record(self):
        audio = self.audio
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        print("recording...")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("recorded...")

        stream.stop_stream()
        stream.close()

        with wave.open(self.OUTPUT_FILE, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))

        return self.OUTPUT_FILE

