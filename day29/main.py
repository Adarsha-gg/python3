
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    pass_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters)  for number in range(nr_letters)]
    password_symbol = [random.choice(symbols)  for number in range(nr_symbols)]
    password_number = [random.choice(numbers)  for number in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join (password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
        "email":email,
        "password":password
        } 
    }
  
    if website == "" or password == "":
        messagebox.showinfo(title="STOP",message="Dont leave the fields empty")
    else:
        try:
            with open('day29\data.json','r') as file:
                #read old data
                data = json.load(file)               
        except FileNotFoundError:
            with open('day29\data.json','w') as file:
                json.dump(new_data, file,indent=4)
        else: #updated data
            data.update(new_data)
            with open('day29\data.json','w') as file:
                json.dump(new_data, file,indent=4)
        finally:         
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

def search():
    website = website_entry.get()
    try:
        with open("day29\data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Details",message=" NO SUCH FILE FOUND")
    else: 
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Details",message=data[website])
        else:
             messagebox.showinfo(title="Details",message="No details")      
      
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="day29\logo.png")
canvas.create_image(100,100,image = photo)


#labels
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)

email_label = Label(text="Email/Username:")
email_label.grid(row = 2, column = 0)

pass_label = Label(text="Password:")
pass_label.grid(row = 3, column = 0)

#buttons
generate_button = Button(text="Generate Password",command=generate)
generate_button.grid(row=3,column=2)

add_button = Button(text= "Add",width=36,command=add)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=10,command=search)
search_button.grid(row=1,column=3)

#entry
website_entry = Entry(width=35)
website_entry.grid(row =1 , column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width= 35)
email_entry.grid(row =2 , column=1,columnspan=2)
email_entry.insert(0,"adarshamishra33@gmail.com")

pass_entry = Entry(width= 17)
pass_entry.grid(row =3 , column=1)

window.mainloop()