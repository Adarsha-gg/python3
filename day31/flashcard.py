from tkinter import *
from turtle import width
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
def generate():
    with open(file="day31\data/french_words.csv") as file:
        num = random.randint(0,102)
        data = pandas.read_csv(file)
        french_word =data['French'][num]
        return french_word
        
def change():
    global french
    french = generate()
    canvas.itemconfig(ez,text=french)
#window
window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#canvas
canvas = Canvas(width=800,height=526 , highlightthickness= 0,bg=BACKGROUND_COLOR)
photo = PhotoImage(file="D:\Code\python\day31\images\card_front.png")
canvas.create_image(400, 250, image=photo)
enter= "French"
ez= canvas.create_text(400,150,text=enter,font=("Ariel",40,"italic"))

word = canvas.create_text(400,260,text=french,font=("Ariel",60,"italic"))
canvas.grid(column=0,row=0,columnspan=2)




#buttons
cross_image = PhotoImage(file="day31\images\wrong.png")
cross = Button(image=cross_image, highlightthickness=0,command=change)
cross.grid(column=0,row=1)

right_image = PhotoImage(file="day31\images/right.png")
right = Button(image=right_image, highlightthickness=0)
right.grid(column=1,row=1)









window.mainloop()