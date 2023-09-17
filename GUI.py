import psutil
import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("dark")
msglist = []

app = ctk.CTk()
app.title("Athar")

window_width = 1280
window_height = 720

# get the screen dimension
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


frame = ctk.CTkFrame(master=app, width=200, height=200)

free_mem = psutil.virtual_memory().free / 1073741824


if(free_mem > 10):
        best_model = "large"
elif(free_mem > 5):
        best_model = "medium.en"
elif(free_mem > 2):
        best_model = "small.en"
elif(free_mem > 1):
        best_model = "base.en"
elif(free_mem > 0):
        best_model = "tiny.en"

StateLabel = ctk.CTkLabel(master=app, text=best_model, font= ("serif", 16))
StateLabel.pack(side=ctk.BOTTOM)

def Send(text):
        if len(msglist) % 2 == 0:
                color = ("#4C4E52")
        else:
                color = ("#6F7378")
        height = ((len(text) * 16 / 1280) * 50) /3.5
        textbox = ctk.CTkTextbox(master=app, font = ("serif", 16), width=1280, height=height, fg_color=color)
        textbox.insert("0.0", text)
        textbox.configure(state="disabled")
        textbox.pack()
        msglist.append(textbox)
        app.update()