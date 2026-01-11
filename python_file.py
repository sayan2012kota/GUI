from tkinter import *
from tkinter.filedialog import askopenfile
def open_file():
    file = askopenfile(mode="r", filetypes=[("Python Files", "*.py")])
    if file is not None:
        data = file.read()
        print(data)
window = Tk()
window.geometry("300x300")
button = Button(window, text = "open file?", command=open_file)
button.place(x=100, y=100)




window.mainloop()