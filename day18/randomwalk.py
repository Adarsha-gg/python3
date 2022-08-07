import turtle as t
import random
stop = False
tim = t.Turtle()
tim.shape("arrow")
tim.color("black")

move =[90,180,270,360]
tim.speed("fast")
tim.pensize(8)
t.colormode(255)
def rcolor():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = (r, g, b)
    return color

def movee():
    g = random.choice(move)
    ez = rcolor()
    tim.left(g)
    tim.forward(20)
    tim.color(ez)

while stop != True:
    movee()

screen = t.Screen()
screen.exitonclick()