
from quiz_brain import QuizBrain
from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain): #insues that the paramater passed is a object of the class quizbrain
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        #canvas
        self.canvas = Canvas(height=250,width=300,bg="white")
        self.ques = self.canvas.create_text(150, 125, text="" ,width=290, font=("Arial", 20, "bold"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        #labels        
        self.score = Label(text="Score:0", bg= THEME_COLOR , fg="White")
        self.score.grid(row=0,column=1)

        #images
        tick = PhotoImage(file="day34\images/true.png")
        cross = PhotoImage(file="day34\images/false.png")

        #buttons
        self.rightt = Button(image=tick, highlightthickness=0,command = self.right)
        self.rightt.grid(row=2,column=0)

        self.cross = Button(image=cross, highlightthickness=0,command= self.wrong)
        self.cross.grid(row=2,column=1)
        
        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text= q_text)
        else:
            self.canvas.itemconfig(self.ques, text= "THIS IS THE END") 
            self.canvas.config(bg="white")
            self.rightt.config(state="disabled")
            self.cross.config(state="disabled")  

    def right(self):
        right = self.quiz.check_answer("True")
        self.feedback(right)
        

    def wrong(self):
        wrong = self.quiz.check_answer("False")   
        self.feedback(wrong)
        

    def feedback(self,right):
        if right is True:
            self.canvas.config(bg="Green")
        elif right is False:
            self.canvas.config(bg="Red")    
        self.window.after(1000,self.get_next_ques)
