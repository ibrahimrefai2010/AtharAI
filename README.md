![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![html](https://img.shields.io/badge/HTML-red?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-purple?style=flat-square) ![GPT](https://img.shields.io/badge/GPT-4.5_Turbo-Green?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-1.0_Pro-white?style=flat-square) ![TTS](https://img.shields.io/badge/Speech_To_Text-Whisper-yellow?style=flat-square) ![STT](https://img.shields.io/badge/Text_To_Speech-Pyttsx3-Blue?style=flat-square&color=LightBlue) ![Flask](https://img.shields.io/badge/Flask-red?style=flat-square)

<h1> What Is It? </h1>
It's the first voice assistant that uses LLMs as it's underlying technology, LLMs means large language models, like ChatGPT and Gemini. <br> 
our competitors like siri and google assistant use a hardcoded method which makes the voice assistant dumb, but AtharAI is not like them because it's using Machine learning which makes it miles ahead of it's competition.

<h1>How to install</h1>
1- Create a python 3.10 Virtual enviroment and activate it. <br>
2- Dowload ffmpeg using <code>winget install ffmpeg</code> <br>
3- download the needed python modules:<br> <code>pip install -q -U psutil SpeechRecognition pyaudio openai==0.28 pyttsx3 flask waitress google-generativeai openai-whisper</code> <br>

<h1> How to use: </h1>
Fire up Main.py and that's it.

<h2>How to switch models</h2>
AtharAI supports both Gemini 1.0 pro by Google, or GPT-4-Turbo by OpenAI, GPT-4-Turbo is more powerful, but AtharAI uses Gemini-1.0-pro by default, here's how you can switch: <br>
1- open up <code>pre.py</code> there you can find the API keys, and the model used <br>
2- to switch to GPT-4-turbo you have to insert you own OpenAI key<br>
3- after inserting your key you can change the <code>model</code> value from <code>"gemini"</code> to <code>"gpt"</code>, then save the changes and run the app, and you'll be using GPT-4-Turbo.

<h1>AtharAI V2.0, what's new:</h1>
it now uses HTML, CSS, JS as it's GUI instead of tkinter. <br>
Much simpler installation process <br>
Now uses GPT-4-Turbo or Gemini 1.0 pro preferably, instead of GPT-3.5-Turbo. <br>
All known bugs in AtharAI V1 resolved  <br>
