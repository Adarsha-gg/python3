import turtle
class Ball(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.speed = 0.05

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def collide(self):    
        self.ymove *= -1

    def collidepaddle(self):
        self.xmove *= -1
        
    def reset(self):
        self.goto(0,0)    
        self.collidepaddle()

    def hard(self):
        self.speed *=0.9    