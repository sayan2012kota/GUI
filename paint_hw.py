from tkinter import *
from tkinter.colorchooser import askcolor
window = Tk()
window.geometry("400x600")
def red():
    global current_colour
    current_colour = "red"
def blue():
    global current_colour
    current_colour = "blue"
def green():
    global current_colour
    current_colour = "green"
def yellow():
    global current_colour
    current_colour = "yellow"


def draw(event):
    global x
    global y
    global current_colour
    width = scale.get()
    if active_button == button3:
        active_colour = "white"
    if active_button == button:
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
def use_eraser():
    global active_button
    button3.config(relief=SUNKEN)
    active_button.config(relief=RAISED)
    active_button = button3
current_colour = "black"
x = None
y = None
button = Button(window, text = "pen", command=use_pen)
button.place(x=10, y=10)
active_button = button
button3 = Button(window, text = "eraser", command = use_eraser)
button3.place(x=50, y=10)
button4 = Button(window, text = "Clear", command = clear)
button4.place(x=350, y=10)
button5 = Button(window, bg="red", command = red, width=2)
button5.place(x=120, y=10)
button6 = Button(window, bg="blue", command = blue, width=2)
button6.place(x=150, y=10)
button7 = Button(window, bg="green", command = green, width=2)
button7.place(x=180, y=10)
button8 = Button(window, bg="yellow", command = yellow, width=2)
button8.place(x=210, y=10)
scale = Scale(window, from_=1, to=25, orient=HORIZONTAL)
scale.place(x=240, y=10)
canvas = Canvas(window, bg="white", width=400, height=550)
canvas.place(x=0, y=50)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release)



window.mainloop()
