import pre
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
import json
from lights_cotrol import toggle_lights


def initializeAI():
    global chat_session
    GOOGLE_API_KEY = pre.GOOGLE_API_KEY
    genai.configure(api_key=GOOGLE_API_KEY)

    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-pro",
      generation_config=generation_config,
      tools = [
        genai.protos.Tool(
          function_declarations = [
            genai.protos.FunctionDeclaration(
              name = "toggle_light",
              description = "Toggles the state of the lights (ON/OFF)",
              parameters = content.Schema(
                type = content.Type.OBJECT,
                enum = [],
                required = ["state"],
                properties = {
                  "state": content.Schema(
                    type = content.Type.STRING,
                  ),
                },
              ),
            ),
          ],
        ),
      ],
    )

    chat_session = model.start_chat(
        history=[
        ]
    )


def sendMessage(message): ##adds a new message to the conversation object, and formats the reply
    response = chat_session.send_message(message)
    proccessed_response = process_model_response(response)
    return proccessed_response

def check_if_function_call(response):
    core = response.candidates[0].content.parts[0]
    if 'text' in core:
        return False
    elif 'function_call' in str(core):
        return True

def process_model_response(response):

    if check_if_function_call(response):
        response = str(response.candidates[0].content.parts[0].function_call)
        if 'ON' in response:
            state = 'on'
        elif 'OFF' in response:
            state = 'off'
        toggle_lights(state)
        return f'Turning the lights {state}'
    else:
        return response.candidates[0].content.parts[0].text

