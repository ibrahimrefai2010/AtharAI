<h1> What Is It? </h1>
Athar AI is a speaking version of ChatGPT.

<h2> How to use: </h2>
1- Fire up Main.py <br>
2- when your time to talk a microphone icon will pop on the taskbar <br>
<b>BONUS</b>-  and if you are on mac or Linux you can speak when console tells you to, the annoyment will be removed as soon as possible, so this is just a temporary solution. <br>
3- After you speak Athar will respond.

<h1>Prerequisites</h1>
1- ffmpeg. you can download it via chocolatey <br>
2- run the following command: <br>
<code>pip install git+https://github.com/openai/whisper.git  && pip install psutil && pip install SpeechRecognition && pip install pyaudio && pip install openai && pip install pyttsx3 && pip install customtkinter</code>


<h2>What is Medium.en , small.en, etc?</h2>
It's the of the size voice recognition model that you are using, the bigger the better, but you will need more RAM to run the bigger model, so the program will auto-choose a model for you based on how much <b>free</b> memory you have (it will be replaced remove the annoyment we talked about earlier)

<h2>Checklist</h2>
1- Remove the annoyment by putting it in the place of the model size
The ISSUE: GUI isn't Updating properly which makes it ignore requests to change the text
Possible Fix: Multithreading <br>
2-realistic Voices <br>
3-Foreign language support. <br>
How: by adding translating layers.
