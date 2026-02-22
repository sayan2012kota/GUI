from tkinter import *
from tkinter.filedialog import *
window = Tk()
window.geometry("700x450")
def delete_file():
    selected_file = listbox.curselection()
    listbox.delete(selected_file)
def add_file():
    listbox.insert(END, entry.get())
    entry.delete(0, END)
def save_file():
    saved_file = asksaveasfile(defaultextension=".txt")

#def open_file():


button =  Button(window, text = "SAVE", command = save_file)
button.place(x=325, y=5)
entry = Entry(window)
entry.place(x=275, y=40)
button2 = Button(window, text = "ADD", command = add_file)
button2.place(x=326, y=65)
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
listbox = Listbox(window, height = 15, width=50, yscrollcommand=scrollbar.set, bg= "crimson", fg="black")
scrollbar.config(command=listbox.yview)
listbox.place(x=175, y=150)
for i in range(30):
    listbox.insert(END, "List" +  str(i))
button3 = Button(window, text = "OPEN", width = 15, )
button3.place(x=45, y=180)
button4 = Button(window, text = "DELETE", width = 15, command = delete_file)
button4.place(x=550, y=180)












window.mainloop()