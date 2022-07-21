import turtle as t

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)  

def move_right():
    tim.right(10)  

def move_left():
    tim.left(10)  

def clear():
    t.resetscreen()
    tim.home()

tim =t.Turtle()
screen = t.Screen()
screen.listen()

screen.onkey(key = "w", fun = move_forward )
screen.onkey(key = "s", fun = move_backward )
screen.onkey(key = "a", fun = move_left )
screen.onkey(key = "d", fun = move_right )
screen.onkey(key = "c", fun = clear )
screen.exitonclick()