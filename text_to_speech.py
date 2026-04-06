from tkinter import *
from gtts import gTTS 
import os
window = Tk()
window.geometry("300x400")
def play_speech():
    text = entry.get()
    converted_text = gTTS(text=text, lang="en", slow=False)
    converted_text.save("audio.wav")
    os.system("audio.wav")
label = Label(window, text = "Text to Speech", width= "15", font = (15))
label.place(x = 50, y=10)
entry = Entry(window, width = "20")
entry.place(x=50, y = 175)
button = Button(window, text = "Convert", command = play_speech)
button.place(x = 100, y=300)












window.mainloop()