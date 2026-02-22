from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry("400x400")
def make_table():
    table = ""
    for i in range(radio_number.get()):
        table = table + str(number.get()) + "X"+ str(i+1) + "=" + str(number.get()*(i+1)) + "\n"
        print(table)
    label3.configure(text = table)
label = Label(window,text = "Select a number:" )
label.grid(row=0, column=0, columnspan=3, pady=20)
label2 = Label(window, text = "Select the number and range:")
label2.grid(row=1, column=0, padx=25)
number = IntVar()
combobox = Combobox(window, textvariable=number, width = 2)
combobox.grid(row = 1, column=1)
combobox["values"]=tuple(range(100))
radio_number = IntVar()
radiobutton = Radiobutton(window, text = "10", variable = radio_number, value = 10)
radiobutton.grid(row=1, column=2, padx=25)
radiobutton2 = Radiobutton(window, text = "20", variable = radio_number, value = 20)
radiobutton2.grid(row=2, column=2, padx=25)
radiobutton3 = Radiobutton(window, text = "30", variable = radio_number, value = 30)
radiobutton3.grid(row=3, column=2, padx=25)
radio_number.set(10)
label3=Label(window, anchor="center")
label3.place(x=150, y=100)
button = Button(window, text = "Create multiplication table", command = make_table)
button.place(x=170,y=350)






























window.mainloop()
