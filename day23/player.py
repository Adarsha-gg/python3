import turtle
Starting = (0,-280)
FINISH_LINE_Y = 280
class Player(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(Starting)
        self.left(90)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)

    def go_to_start(self):
        self.goto(Starting)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False    