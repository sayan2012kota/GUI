from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry("400x400")
progress_bar = Progressbar(window, orient=HORIZONTAL, length = 200, mode = "determinate")
progress_bar.place(x=100, y=100)

window.mainloop()