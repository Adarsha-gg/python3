from tkinter import *

import pandas
import random

num = {}
to_learn= {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("day31\data/to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("day31\data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

def generate():
    photo = PhotoImage(file="D:\Code\python\day31\images\card_front.png")
    canvas.itemconfig(canvas_image,image=photo)
    canvas.itemconfig(ez,text="French")
    global num,flip_timer
    num = random.choice(to_learn)
    french_word =num['French']
    canvas.itemconfig(word,text=french_word)
    flip_timer = window.after(3000,func=flip)

def flip():
    english_word =num['English']
    photo2 = PhotoImage(file="D:\Code\python\day31\images\card_back.png")
    canvas.itemconfig(canvas_image,image=photo2)
    canvas.itemconfig(ez,text="English")
    canvas.itemconfig(word,text=english_word)
    
def is_known():
    to_learn.remove(num)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    generate()   

#window
window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)
#canvas
canvas = Canvas(width=800,height=526 , highlightthickness= 0)
photo = PhotoImage(file="D:\Code\python\day31\images\card_front.png")
canvas_image = canvas.create_image(400, 250, image=photo)
ez= canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word = canvas.create_text(400,260,text="Start",font=("Ariel",60,"italic"))
canvas.grid(column=0,row=0,columnspan=2)


#buttons
cross_image = PhotoImage(file="day31\images\wrong.png")
cross = Button(image=cross_image, highlightthickness=0,command=generate)
cross.grid(column=0,row=1)

right_image = PhotoImage(file="day31\images/right.png")
right = Button(image=right_image, highlightthickness=0,command=generate)
right.grid(column=1,row=1)





generate()



window.mainloop()