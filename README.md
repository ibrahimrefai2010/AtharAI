![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![html](https://img.shields.io/badge/HTML-red?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-purple?style=flat-square) ![GPT](https://img.shields.io/badge/GPT-4.5_Turbo-Green?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-1.0_Pro-white?style=flat-square) ![TTS](https://img.shields.io/badge/Speech_To_Text-Whisper-yellow?style=flat-square) ![STT](https://img.shields.io/badge/Text_To_Speech-Pyttsx3-Blue?style=flat-square&color=LightBlue) ![Flask](https://img.shields.io/badge/Flask-red?style=flat-square)

<h1> What Is It? </h1>
It's Jarvis Except that it's Real 🤖.

<h2> How to use: </h2>
1- Fill in the variables in pre.py <br>
2- Fire up Main.py <br>
3- when your time to talk a microphone icon will pop on the taskbar <br>
<b>BONUS</b>-  and if you are on mac or Linux you can speak when console tells you to, the annoyment will be removed as soon as possible, so this is just a temporary solution. <br>
4- After you speak Athar will respond.

<h1>How to install</h1>
1- Download ffmpeg, you can download it via chocolatey. <br>
2- You need to have to Git installed on your machine. <br>
3- An OpenAI key. <br>
4- Run the following command: <br>
<code>pip install git+https://github.com/openai/whisper.git  && pip install psutil && pip install SpeechRecognition && pip install pyaudio && pip install openai==0.28 && pip install pyttsx3 && pip install customtkinter && pip install pvcheetah && pip install PySide2 && pip install -q -U google-generativeai</code> <br>
5- Assign your name and most importantly your OpenAI key in pre.py


<h2>What is Medium.en , small.en, etc?</h2>
It's the of the size voice recognition model that you are using, the bigger the better, but you will need more RAM to run the bigger model, so the program will auto-choose a model for you based on how much <b>free</b> memory you have (it will be replaced to remove the annoyment aforementioned)

<h2>Checklist</h2>
1- Remove the annoyment aforementioned by putting it in the place of the model size <br>
The ISSUE: GUI isn't Updating properly which makes it ignore requests to change the text <br>
Possible Fix: Multi-Threading <br>
2- Add scrolling.<br>
ISSUE: When messages go below the windows size you can't see the new messages <br>
Possible Fix: Remake the UI (With Multi-threading to fix issue number 1) <br>
3-realistic Voices <br>
4-Foreign language support. <br>
How: by adding translating layers.<br>

<h1>AtharAI V2.0 is in it's final stages and is coming soon, what's new:</h1>
it now uses HTML, CSS, JS as it's GUI instead of tkinter. <br>
Much simpler installation process <br>
Now uses GPT-4-Turbo or Gemini 1.0 pro preferably, instead of GPT-3.5-Turbo. <br>
All known bugs in AtharAI V1 resolved <br>
