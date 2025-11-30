from tkinter import *
window = Tk()
window.config(background = "red")
window.geometry("500x500")
window.resizable(False, False)
label = Label(window, text = "login:")
label.place(x=100, y=100)


window.mainloop()