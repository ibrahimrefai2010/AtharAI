import openai


def initializeAI(API_KEY):
    openai.api_key = API_KEY
    global messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


def sendMessageToAI(inputMessage):
    messages.append({"role": "user", "content":inputMessage})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages)
    response = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": response})
    return response