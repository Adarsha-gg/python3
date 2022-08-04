import tkinter

#main display screen

window = tkinter.Tk()
window.title("Mile to Km converter") #windows name
window.minsize(width=600 , height= 600)
window.config(padx= 10 , pady= 10) 

#for clicking
def click():
    miles = int(entry.get())
    km = miles*1.6
    label4.config(text= km)

#entry
entry = tkinter.Entry()
entry.grid(row=0, column= 2)

#Label
label = tkinter.Label(text="Miles", font=("Arial",10))
label.grid(column =  3, row = 0)  #display into the screen

label2 = tkinter.Label(text="is equal to", font=("Arial",12))
label2.grid(column =  1, row = 1)  #display into the screen

label3 = tkinter.Label(text="KM", font=("Arial",10))
label3.grid(column =  3, row = 1)  #display into the screen

label4 = tkinter.Label(text="0", font=("Arial",10))
label4.grid(column =  2, row = 1)

#button
button = tkinter.Button(text="Calculate" , command= click)
button.grid(column=3 , row= 3)

window.mainloop()  #always at the end