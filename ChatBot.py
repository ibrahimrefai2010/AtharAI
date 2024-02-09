import openai 
import pre

def initializeAI():
	openai.api_key = pre.OPENAI_API_KEY
	global messages
	messages = [ {"role": "system", "content": 
				"You are a intelligent assistant."} ] 


def sendMessageToAI(message):
	messages.append({"role": "user", "content": message}) 
	chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 
	reply = chat.choices[0].message.content 
	print(f"{reply}") 
	messages.append({"role": "assistant", "content": reply}) 
	return (f"{reply}")
 