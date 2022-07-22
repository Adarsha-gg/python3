from turtle import Turtle
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,280)
        self.update()

    def update(self):
        self.write(f"Score:{self.score}",align = ALIGN)

    def increase(self):    
        self.score +=1
        self.clear()
        self.update()
        
    def over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGN)
        
    

