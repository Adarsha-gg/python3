
from distutils.command.config import config
from tkinter import *
import math
from turtle import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    label.config(text="Timer")
    canvas.itemconfig(time_text,text="00:00")
    check_marks.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work = WORK_MIN * 60
    s_break = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60
    reps += 1
  
    if reps % 8 == 0:
        countdown(l_break)
        label.config(text= "LONG BREAK",fg= YELLOW)
        reps += 1

    elif reps % 2 != 0:
        countdown(work)
        label.config(text= "WORK",fg= PINK)
        reps += 1

    elif reps % 2 == 0:
        countdown(s_break)
        label.config(text= "SHORT BREAK",fg= RED)
        reps += 1   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text= f"{count_min}:{count_sec}")
    
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count -1)
    
    else:
        start_timer()
        mark = ""
        for ez in range(math.floor(reps/2)):
            mark += "✔"
        check_marks.config(text = mark)    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100 , pady= 100, bg= GREEN)


#label
label = Label(text="Timer", font= (FONT_NAME,28,"bold"),bg=GREEN, fg= RED)
label.grid(column=2 , row= 1)

#canvas
photo = PhotoImage(file="day28/tomato.png")
canvas = Canvas(width=300,height=300, bg= GREEN, highlightthickness= 0)
canvas.create_image(150,150,image = photo)
global textt
textt = "00:00"
time_text = canvas.create_text(150, 170, text= textt, font= (FONT_NAME,30,"bold"), fill= "black")
canvas.grid(column=2 , row=2)

#button
start = Button(text="Start",command= start_timer)
start.grid(column=1,row=3)

end = Button(text="Stop", command= reset_timer)
end.grid(column=3,row=3)

#check_marks
check_marks = Label(highlightthickness= 0,bg= GREEN)
check_marks.grid(column=2,row=4)


window.mainloop()
