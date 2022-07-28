import turtle as t

POSITIONS =[(0,0),(-20,0),(-30,0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.squares =[]
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in POSITIONS:
            self.addsquares(position)

    def extend(self):
        self.addsquares(self.squares[-1].position())
        
    def addsquares(self,position):
        tim = t.Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.squares.append(tim)

    def move(self):            
        for num in range(len(self.squares)-1, 0, -1):
            new_x =self.squares[num-1] .xcor()
            new_y =self.squares[num-1] .ycor()
            self.squares[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)   

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
      
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def reset(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake() 
        self.head = self.squares[0]   