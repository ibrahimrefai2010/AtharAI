import Voice_Recognition as VR
import Text_to_speech as TTS
import GUI as UI
import ChatBot
import pre


AIName = ("Athar")
PersonName = pre.FULL_NAME

ChatBot.initializeAI(pre.OPENAI_API_KEY)

Chatbot_output = ChatBot.sendMessageToAI("Hello, my name is " + PersonName).replace("Chatgpt", AIName).replace("ChatGPT", AIName)
UI.Send(Chatbot_output)
TTS.Say(Chatbot_output)


while True:
        Input = VR.Input_user()
        UI.Send(Input)

        if (Input == ""): 
                Input = VR.Input_user()
        else:
                Chatbot_output = ChatBot.sendMessageToAI(Input).replace("Chatgpt", AIName).replace("ChatGPT", AIName).replace("GPT", AIName).replace("GPT-3", AIName).replace("OpenAI", "Ibraim Refai")
                UI.Send(Chatbot_output)
                TTS.Say(Chatbot_output)