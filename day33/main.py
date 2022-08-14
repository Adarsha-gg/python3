
from cgitb import text
from tkinter import *
import requests
data ={}
def get_quote():
   kanye = requests.get("https://api.kanye.rest")
   kanye.raise_for_status()
   quote = kanye.json()
   data = quote["quote"]
   canvas.itemconfig(quote_text,text=data)
   


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="" ,width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day33\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()