from tkinter import *
import random
from tkinter import messagebox
window = Tk()
window.geometry("400x500")
word_list = ["satisfied", "scrape","seize","policeman","buttocks","trouble","weave","scream","load","clarify"]
word_choice = random.choice(word_list)
word = list(word_choice)
random.shuffle(word)
shuffled_word = "".join(word)
print(shuffled_word)
score = 0
def choose_new_word():
    global word_choice
    word_choice = random.choice(word_list)
    word = list(word_choice)
    random.shuffle(word)
    shuffled_word = "".join(word)
    label2.config(text = shuffled_word)
    
def check_answer():
    global score
    answer = entry.get()
    if answer == word_choice:
        score = score + 1
        messagebox.showinfo("Result", "Your answer was right")
    else:
        messagebox.showinfo("Result", "Your answer was wrong")
    print(score)
    choose_new_word()
    label3.config(text = str(score))
    entry.delete(0, END)
def reset():
    global score
    score = 0
    choose_new_word()
    label3.config(text = str(score))
    entry.delete(0, END)



label = Label(window, text = "JUMBLED WORD GAME")
label.place(x=50, y=20)
label2 = Label(window, text = shuffled_word)
label2.place(x = 100, y=100)
entry = Entry(window)
entry.place(x=150, y=200)
button = Button(window, text = "Check", command = check_answer)
button.place(x=150, y = 300)
button2 = Button(window, text = "Reset", command = reset)
button2.place(x=150, y=350)
label3 = Label(window, text = score)
label3.place(x = 10, y=475)














window.mainloop()
