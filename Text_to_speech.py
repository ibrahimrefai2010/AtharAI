def Say(Text): #gets the text from main.py and coverts it into speech
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(Text)
        engine.runAndWait()