import turtle

POSITION = (-365,365)
class Paddle(turtle.Turtle):
        def __init__(self,positionn) -> None:
                super().__init__()
                
                self.shape("square")
                self.color("white")
                self.penup()
                self.shapesize(5,1)
                self.goto(positionn)

        def up(self):
                new_y = self.ycor() + 20
                self.goto(self.xcor(), new_y)

        def down(self):
                new_y = self.ycor() - 20
                self.goto(self.xcor(), new_y)
        
        def right(self):
        
                new_x = self.xcor() + 20
                self.goto(new_x, self.ycor())

        def left(self):
                new_x = self.xcor() - 20
                self.goto(new_x, self.ycor())