import GPT
import Gemini
import queue
def initializeAI(model, name): #initializes the model based on the prefered model chosen by the user in pre.py
    global AI
    global AIName
    AIName = name
    AI = model
    if AI == "gpt":
        GPT.initializeAI()
    elif AI == "gemini":
        Gemini.initializeAI()
    else:
        raise "AI unknown in Chatbot.initializeAI"

def sendMessage(message): #sends a message to the model based on the prefered model chosen by the user in pre.py
    returned_message = ""
    if AI == "gpt":
        returned_message = GPT.sendMessage(message)
    elif AI == "gemini":
        returned_message = Gemini.sendMessage(message)
    else:
        raise "AI unknown in Chatbot.sendMessageToAI"
    return returned_message.replace("Chatgpt", AIName).replace("ChatGPT", AIName).replace("[your_name]", AIName).replace("Gemini", AIName).replace("Google", "Ibrahim Refai").replace("OpenAI", "Ibrahim Refai")