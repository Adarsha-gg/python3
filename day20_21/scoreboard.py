from turtle import Turtle
ALIGN = "center"
with open(r'D:\Code\python\day20_21\highscore.txt') as file:
        content = int(file.read())
        
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = content
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.high_score}",align = ALIGN)

    def increase(self):    
        self.score +=1
        
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'D:\Code\python\day20_21\highscore.txt','w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()
        
       
        
    #def over(self):
        #self.goto(0,0)
        #self.write("GAME OVER", align= ALIGN)
        
    

