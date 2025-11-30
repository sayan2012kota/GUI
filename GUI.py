from tkinter import *
window = Tk()
window.config(background = "blue")
window.geometry("500x500")
window.resizable(False, False)
entry = Entry(window, width = 23)
entry.place(x= 150, y = 250)
label = Label(window, text = "Here is the button", background = "green", font = ("Calibra", 15 ))
label.place(x=250, y = 150)
button = Button(window, text = "Click this!", background="red", fg="black", command=window.destroy)
button.place(x=250, y=250)




















window.mainloop()