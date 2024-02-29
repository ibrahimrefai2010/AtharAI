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
5- Run the following command: <br>
<code>pip install git+https://github.com/openai/whisper.git  && pip install psutil && pip install SpeechRecognition && pip install pyaudio && pip install openai==0.28 && pip install pyttsx3 && pip install customtkinter && pip install pvcheetah && pip install PySide2</code> <br>
6- Assign your name and most importantly your OpenAI key in pre.py


<h2>What is Medium.en , small.en, etc?</h2>
It's the of the size voice recognition model that you are using, the bigger the better, but you will need more RAM to run the bigger model, so the program will auto-choose a model for you based on how much <b>free</b> memory you have (it will be replaced remove the annoyment we talked about earlier)

<h2>Checklist</h2>
1- Remove the annoyment by putting it in the place of the model size <br>
The ISSUE: GUI isn't Updating properly which makes it ignore requests to change the text <br>
Possible Fix: Multi-Threading <br>
2- Add scrolling.<br>
ISSUE: When messages go below the windows size you can't see the new messages <br>
Possible Fix: Remake the UI (With Multi-threading to fix issue number 1) <br>
3-realistic Voices <br>
4-Foreign language support. <br>
How: by adding translating layers.
