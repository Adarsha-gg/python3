from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20)
canvas = Canvas(width=300,height=300)
photo = PhotoImage(file="day29\logo.png",width=200,height=200)
canvas.create_image(150,150,image = photo)
canvas.grid(column=1,row=1)










window.mainloop()