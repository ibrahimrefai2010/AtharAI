#this is the file resposinble for the gpt-4-turbo model
import openai 
import pre

def initializeAI(): #makes the conversation object such that the Ai remembers what the user said
	print("initializeAI called")
	openai.api_key = pre.OPENAI_API_KEY
	global messages
	messages = [ {"role": "system", "content": 
				"You are a intelligent assistant."} ] 

def sendMessage(message): #adds a new message to the conversation object, and sends the conversation object to the model, formats the reply.
	messages.append({"role": "user", "content": message}) 
	chat = openai.ChatCompletion.create(model="gpt-4-turbo-preview", messages=messages) 
	reply = chat.choices[0].message.content 
	print(f"{reply}") 
	messages.append({"role": "assistant", "content": reply}) 
	return (f"{reply}")