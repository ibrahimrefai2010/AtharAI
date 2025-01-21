def Input_user():  
    import speech_recognition as sr
    import whisper
    import os
    import time
    import app
    time.sleep(0.5)
    def main():
        app.SetSpeaker('user') #Sets the mic icon, so it indicates that the user should talk now
        print("Speak")
        r = sr.Recognizer()
    
        with sr.Microphone() as source: #recordes whatthe user said and saves it to recorded.wav, when the user finishes talking it automatically saves the data from RAM to the disk, for the next step
            

            r.adjust_for_ambient_noise(source)
    
            audio = r.listen(source)
            app.SetSpeaker('Athar')
            print("Recognizing Now .... ")

    
            # write audio
            with open("recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())
 
    main()
    



    model = whisper.load_model("small.en") #uses the openAI whisper model to recognize turn what the user said into text, for the model to reply
    
    result = model.transcribe("recorded.wav")

    return result["text"]