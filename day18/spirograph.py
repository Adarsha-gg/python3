import turtle as t 
import random
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.pensize(1)
def rcolor():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = (r, g, b)
    return color

for i in range(1,100):
    tim.circle(100)
    tim.right(5)
    g = rcolor()
    tim.color(g)
    
screen = t.Screen()
screen.exitonclick()    