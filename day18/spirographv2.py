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

def draw(size_p):
    for i in range(int(360/size_p)):
        tim.circle(100)
        tim.setheading(size_p + tim.heading())
        
        tim.color(rcolor())

size = int(input("Size of gap between the circles: "))
draw(size)


        
screen = t.Screen()
screen.exitonclick()    