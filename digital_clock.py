from tkinter import *
from time import strftime
window = Tk()
window.geometry("300x300")
label = Label(window)
label.place(x=100, y=100)
def get_time():
    time = strftime("%H:%M:%S %p")
    label.config(text=time)
    label.after(1000, get_time)
get_time()



window.mainloop()