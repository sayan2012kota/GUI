from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x400")
label = Label(window, text = "Message Boxes")
label.place(x=200, y=200)
messagebox.showinfo("information", "Here is the info")
messagebox.showwarning("Warning!", "Are you sure you want to continue?")
messagebox.showerror("ERROR", "There is an error")
messagebox.askquestion("Question", "Would you like to continue")
messagebox.askokcancel("A question", "Do you want to continue?")
messagebox.askyesno("Different question", "Are you willing to continue?")
messagebox.askretrycancel("The end", "Would you like to retry or stop?")

window.mainloop()