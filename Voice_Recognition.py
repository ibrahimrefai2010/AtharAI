def Input_user():  
    import speech_recognition as sr
    import whisper
    import os
    import psutil
    import GUI as UI
    import time
    time.sleep(0.5)
    def main():
        print("Speak")
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            

            r.adjust_for_ambient_noise(source)
    
            audio = r.listen(source)
    
            print("Recognizing Now .... ")

    
            # write audio
            with open("C:\\Users\\abura\\Programming\\AtharAI-main\\recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())
 
    main()
    
    free_mem = psutil.virtual_memory().free / 1073741824

    if(free_mem > 10):
        best_model = "large"
    elif(free_mem > 5):
        best_model = "medium.en"
    elif(free_mem > 2):
        best_model = "small.en"
    elif(free_mem > 1):
        best_model = "base.en"
    elif(free_mem > 0):
        best_model = "tiny.en"


    model = whisper.load_model("medium.en")
    
    result = model.transcribe("C:\\Users\\abura\\Programming\\AtharAI-main\\recorded.wav")

    return result["text"]