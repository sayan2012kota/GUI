from tkinter import *
from tkinter import messagebox
window = Tk()
global_inventory = {}
def clear_entries():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
def add_item():
    x = entry1.get()
    if not x:
        messagebox.showerror("ERROR", "There is an error")
    global_inventory[x]=(entry2.get(), entry3.get(), entry4.get())
    listbox.insert(END, x)
    clear_entries()
def delete_item():
    selected_value = listbox.curselection()
    del global_inventory[listbox.get(selected_value)]
    listbox.delete(selected_value)
window.geometry("500x700")
listbox = Listbox(window, height = 20, width=25)
listbox.place(x=10, y=75)
entry1 = Entry(window)
entry1.place(x=300, y=100)
entry2 = Entry(window)
entry2.place(x=300, y=200)
entry3 = Entry(window)
entry3.place(x=300, y=300)
entry4 = Entry(window)
entry4.place(x=300, y=400)
label1 = Label(window, text = "Product Name:")
label1.place(x=200, y=100)
label2 = Label(window, text = "ID:")
label2.place(x=275, y=200)
label3 = Label(window, text = "Price:")
label3.place(x=260, y=300)
label4 = Label(window, text = "Stock:")
label4.place(x=260, y=400)
add_items = Button(window, text = "Add Item:",  command = add_item)
add_items.place(x = 75, y = 600)
delete_items = Button(window, text = "Delete Selected:", command = delete_item)
delete_items.place(x=250, y=600)


window.mainloop()