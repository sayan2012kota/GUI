from tkinter import *
window = Tk()
window.geometry("400x600")
button = Button(window, text = "pen")
button.place(x=10, y=10)
button2 = Button(window, text = "brush")
button2.place(x=60, y=10)
button3 = Button(window, text = "eraser")
button3.place(x=110, y=10)
button4 = Button(window, text = "Colour")
button4.place(x=160, y=10)
scale = Scale(window, from_=1, to=10, orient=HORIZONTAL)
scale.place(x=210, y=10)
canvas = Canvas(window, bg="white", width=400, height=550)
canvas.place(x=0, y=50)




window.mainloop()
