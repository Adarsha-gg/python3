from cgitb import text
import tkinter


window = tkinter.Tk()
window.title("Hi") #windows name
window.minsize(width=600 , height= 600) 

#Label

label = tkinter.Label(text="LETS GO LABEL", font=("Arial",22))
label.pack()  #display into the screen

#for clicking
def click():

     label.config(text = entry.get()) 


#button
button = tkinter.Button(text="helo" , background="black", command= click)
button.pack()


#ENTRY
entry = tkinter.Entry(width=20)
entry.pack()














window.mainloop()  #always at the end