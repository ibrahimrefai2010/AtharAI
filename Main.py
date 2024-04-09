import Voice_Recognition as VR
import Text_to_speech as TTS
import app
import ChatBot
import pre
import threading
import time
from queue import Queue


def Start_Main():
        app.SetSpeaker('Athar') #Sets the mic icon, so it indicates that the user shouldn't talk now
        PersonName = app.GetName() #gets the name inputed by the user

        ChatBot.initializeAI(pre.MODEL, "Athar") #Intializes the Model from the chatbot.py file

        Chatbot_output = ChatBot.sendMessage("Hello, my name is " + PersonName) #sends a message Containing the user's name, so the AI knows what's the name of the user and returns an output from the model
        chatbot_output_delivered = True 
        '''
        here's a tricky one, since the Flask App is running on a diffrent thread
        if i send the message immediately to the front-end it will result in a race-condtion
        basically, normally when the app is single threaded the commands will execute line-by-line with each line waiting for the one before it to finish
        but here i i'm not single-threaded so if i execute app.SendtoJS directly sendtoJS will finish long before the model finishes and that will result in an error
        beacause sendtoJS is reliant on data from the model it will result in a an error, i order to resolve this, i made this algorithm.
        chatbot_output_delivered is runnning on the same thread as the model so it will never turn true unless the model finishes.
        so i made SendtoJS wait until chatbot_output_delivered turns True, and this resolves the race condition
        '''
        while True:
                if (chatbot_output_delivered == True):
                        app.SendtoJS(Chatbot_output, "Chatbot")
                        break
        TTS.Say(Chatbot_output) #converts the text returned from the model into speech

        while True: #mainloop
                Input = VR.Input_user() #converts the speech by the user into text
                app.SendtoJS(Input, "user")
                
                if (Input == ""): #if there's no text returned, eg. the user didn't talk, it will recogninze again
                        Input = VR.Input_user() 
                else: #sends what the user said in text to the model, then sends what the model said to the frontend and converts it to speech
                        Chatbot_output = ChatBot.sendMessage(Input)
                        app.SendtoJS(Chatbot_output, "Chatbot")
                        TTS.Say(Chatbot_output)


#starts the front-end in a deffrent thread to operate in parallel
GUI_thread = threading.Thread(target=app.start) 
GUI_thread.start()

while True: #waits for the front-end to give clearance to start the app's mainloop this clearance is given through a queue, it is gien when the user gets to the chat page
        if (app.q.empty() == False):
                Start_Main()