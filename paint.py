from tkinter import *
from tkinter.colorchooser import askcolor
window = Tk()
window.geometry("400x600")
def draw(event):
    global x
    global y
    global current_colour
    width = scale.get()
    if active_button == button3:
        active_colour = "white"
    if active_button == button or active_button == button2:
        active_colour = current_colour
    if x and y:
        canvas.create_line(x,y, event.x, event.y, width = width, fill=active_colour, capstyle=ROUND, smooth = TRUE)
    x=event.x
    y=event.y
def release(event):
    global x
    global y
    x=None
    y=None
def clear():
    canvas.delete("all")

def use_pen():
    global active_button
    active_button.config(relief = RAISED)
    button.config(relief=SUNKEN)
    active_button = button
    
def use_brush():
    global active_button
    button2.config(relief=SUNKEN)
    active_button.config(relief=RAISED)
    active_button = button2
def use_eraser():
    global active_button
    button3.config(relief=SUNKEN)
    active_button.config(relief=RAISED)
    active_button = button3
current_colour = "black"
def choose_colour():
    global current_colour
    current_colour = askcolor(current_colour)[1]
    print(current_colour)
x = None
y = None
button = Button(window, text = "pen", command=use_pen)
button.place(x=10, y=10)
active_button = button
button2 = Button(window, text = "brush",  command = use_brush)
button2.place(x=60, y=10)
button3 = Button(window, text = "eraser", command = use_eraser)
button3.place(x=110, y=10)
button4 = Button(window, text = "Colour", command = choose_colour)
button4.place(x=160, y=10)
button5 = Button(window, text = "Clear", command = clear)
button5.place(x=320, y=10)
scale = Scale(window, from_=1, to=25, orient=HORIZONTAL)
scale.place(x=210, y=10)
canvas = Canvas(window, bg="white", width=400, height=550)
canvas.place(x=0, y=50)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release)



window.mainloop()
