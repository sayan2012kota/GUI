from tkinter import *
import random
window = Tk()
window.geometry("400x500")
word_list = ["satisfied", "scrape","seize","policeman","buttocks","trouble","weave","scream","load","clarify"]
word_choice = random.choice(word_list)
word = list(word_choice)
random.shuffle(word)
shuffled_word = "".join(word)
print(shuffled_word)
label = Label(window, text = "JUMBLED WORD GAME")
label.place(x=50, y=20)
label2 = Label(window, text = shuffled_word)
label2.place(x = 100, y=100)
entry = Entry(window)
entry.place(x=150, y=200)
button = Button(window, text = "Check")
button.place(x=150, y = 300)
button2 = Button(window, text = "Reset")
button2.place(x=150, y=350)
label3 = Label(window, text = "")
label3.place(x = 10, y=475)














window.mainloop()
