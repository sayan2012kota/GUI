from tkinter import *
window = Tk()
window.geometry("300x1000")
label = Label(window, text = "Menu")
label.pack(side=TOP)
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
listbox = Listbox(window, height = 20, width=20, yscrollcommand=scrollbar.set, bg= "brown", fg="yellow")
scrollbar.config(command=listbox.yview)
listbox.place(x=50, y=50)
for i in range(30):
    listbox.insert(END, "Pasta", i)




window.mainloop()