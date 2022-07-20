import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("arrow")
tim.color("black")
tim.speed("fastest")
sides = 3
tim.pensize(5)
def rcolor():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = (r, g, b)
    return color

while sides < 10:
   
    g = rcolor()
   
    for i in range(sides):
        tim.right(360/sides)
        tim.forward(50)
        tim.color(g)
    sides += 1

while sides != 2:
    g = rcolor()
    
    for i in range(sides):
        tim.right(360/sides)
        tim.backward(50)
        tim.color(g)
    sides -= 1
    
tim.left(180)
tim.forward(200)

while sides != 10:
    g = rcolor()
    
    for i in range(sides):
        tim.right(360/sides)
        tim.backward(50)
        tim.color(g)
    sides += 1    
screen = t.Screen()
screen.exitonclick()