from gtts import gTTS
from io import BytesIO
from pygame import mixer

def speak(text):
    try:
        mp3_fp = BytesIO()
        
        tts = gTTS(text, lang='en') 
        tts.write_to_fp(mp3_fp)

        mixer.init()

        mp3_fp.seek(0)  
        mixer.music.load(mp3_fp, 'mp3')

        mixer.music.play()

        while mixer.music.get_busy():
            pass

    except Exception as e:
        print(f"Error during text-to-speech: {e}")

speak("Hello, world!")