from tkinter import *
window = Tk()
window.geometry("400x600")
window.title("Music Player")
def play_song():
    index = listbox.curselection()
    song = listbox.get(index)
    label.configure(text = "Now playing..." +  str(song))
button = Button(window, text = "Play", command = play_song)
button.place(x=100, y=50)
listbox = Listbox(window, height = 10, width=20)
listbox.place(x=250, y=0)
listbox.insert(END, "Song" + str(1))
listbox.insert(END, "Song" + str(2))
listbox.insert(END, "Song" + str(3))
listbox.insert(END, "Song" + str(4))
listbox.insert(END, "Song" + str(5))
label = Label(window)
label.place(x=200, y=300)







window.mainloop()
