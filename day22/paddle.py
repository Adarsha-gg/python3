import turtle


class Paddle:
    def __init__(self) -> None:
        
        self.spawn()

    def spawn(self):
      
        paddle = turtle.Turtle()
        paddle.hideturtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.penup()
        paddle.shapesize(5,1)
        paddle.goto(365,0)
        paddle.showturtle()

    def up(self):
            new_y = + 20
            self.head.setheading(UP)

    def down(self):
        
            self.head.setheading(DOWN)
      
    def right(self):
        
            self.head.setheading(RIGHT)

    def left(self):
        
            self.head.setheading(LEFT)