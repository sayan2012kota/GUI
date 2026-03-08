from tkinter import *
window = Tk()
window.geometry("500x500")
def remove_guest():
    selected_file = listbox.curselection()
    listbox.delete(selected_file)
def add_guest():
    listbox.insert(END, entry.get())
    entry.delete(0, END)

entry = Entry(window)
entry.place(x=220,y = 20)
button = Button(window, text = "Add guest", command = add_guest)
button.place(x=240,y=50)
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
listbox = Listbox(window, height = 15, width=50, yscrollcommand=scrollbar.set, bg= "blue", fg="yellow")
listbox.place(x=20, y=80)
scrollbar.config(command=listbox.yview)
button2 = Button(window, text = "Remove selected", command =  remove_guest)
button2.place(x=50, y=30)
































window.mainloop()

