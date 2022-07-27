import turtle

class Level(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,230)
        self.color("white")
        self.current_level = 1
        self.update()

    def update(self):    
        self.clear()
        self.write(self.current_level,font=("Courier",30,"normal"))


    def increase(self):
        self.current_level +=1    
        self.update()


    def over(self):
        self.goto(0,0)
        self.write(f"Game Over",font=("Courier",30,"normal"))    