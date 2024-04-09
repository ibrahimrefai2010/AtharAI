#this is the file resposinble for the gemini 1.0 pro model
import pathlib
import textwrap
import pre

import google.generativeai as genai


def initializeAI():#makes the conversation object such that the Ai remembers what the user said, and defined the model and it's settings
	global convo
	GOOGLE_API_KEY = pre.GOOGLE_API_KEY
	genai.configure(api_key=GOOGLE_API_KEY)
	generation_config = {
	  "temperature": 0.9,
	  "top_p": 1,
	  "top_k": 1,
	  "max_output_tokens": 2048,
	}

	safety_settings = [ #the safety settings
	  {
	    "category": "HARM_CATEGORY_HARASSMENT",
	    "threshold": "BLOCK_ONLY_HIGH"
	  },
	  {
	    "category": "HARM_CATEGORY_HATE_SPEECH",
	    "threshold": "BLOCK_ONLY_HIGH"
	  },
	  {
	    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
	    "threshold": "BLOCK_ONLY_HIGH"
	  },
	  {
	    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
	    "threshold": "BLOCK_ONLY_HIGH"
	  },
	]
	model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
	convo = model.start_chat(history=[])

def sendMessage(message): ##adds a new message to the conversation object, and formats the reply
	#response = model.generate_content(message)
	#processed_response = response.candidates[0].content.parts[0].text
	convo.send_message(message)
	processed_response = convo.last.text
	return processed_response








