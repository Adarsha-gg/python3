import turtle as t
import random
stop = False
tim = t.Turtle()
tim.shape("arrow")
tim.color("black")
tim.speed(10)

move =[90,180,270,360]
tim.speed("fast")
tim.pensize(8)


def movee():
    g = random.choice(move)
    ez = rcolor()
    tim.left(g)
    tim.forward(40)
    tim.color(ez)

while stop != True:
    movee()

screen = t.Screen()
screen.exitonclick()