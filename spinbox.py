from tkinter import *
window = Tk()
window.geometry("300x300")
spinbox = Spinbox(window, from_=0, to=300)
spinbox.place(x=100, y=100)



window.mainloop()