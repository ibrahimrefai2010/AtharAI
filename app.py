#this file is responsible for commuinaction between the frontend and the backend

from flask import Flask, render_template, url_for, request, redirect
from waitress import serve
import webbrowser
from queue import Queue
import time

app = Flask(__name__) 

def SendtoJS(_message, _role): #used by main.py to send messages to the frontend
    global JSONmessage
    JSONmessage = {'message': _message, 'role': _role}

def SetSpeaker(speaking): #used by main.py to set the mic icon
    global currently_speaking
    time.sleep(1)
    currently_speaking = speaking

@app.route("/") #creates the main page in "/" URL
def welcome_page():
    return render_template("index.html")


@app.route("/name") #creates the name page in "/name" URL
def name_page():
    return render_template("name.html")

@app.route('/setname/<name>', methods=['POST']) #a route used by the Frontend to send the name that the user inputed
def SetPersonName(name):
    global FULL_NAME
    FULL_NAME = name
    print(f"app:{FULL_NAME}")
    return ''


@app.route("/chat") #creates the name page in "/loading" URL and gives clearance to main.py to start the mainloop
def chat_page():
    q.put("True")
    return render_template("chat.html")

@app.route('/GetLatestMessage', methods=['POST']) #a route used by the Frontend to check what is the latest message sent by main, this will fire multiple times a second
def GetLatestMessage():
    try:
        return JSONmessage
    except Exception:
        return 'empty'


@app.route('/GetSpeaker', methods=['POST']) #a route used by the Frontend to check who's speaking currently, 'ath' means that athar is now talking, 'user' means that the user is now talking
def GetSpeaker():
    try:
        currently_speakingJSON = {'speaker': currently_speaking}
        return currently_speakingJSON
    except Exception:
        return ""
    
def GetName(): #a method used by main to get the name passed by the frontend
    return FULL_NAME 

def start(): #a method used by main to start the frontend
    global q
    q = Queue() #makes a queue
    host = '127.0.0.1'
    port = '8080'
    webbrowser.open(f"http://{host}:{port}") #opens a browser tab in the URL of the app
    serve(app, port=8080) #starts a WSGI local webserver so, that the frontend lives on it



