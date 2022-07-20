import turtle as t
import random
stop = False
tim = t.Turtle()
tim.shape("arrow")
tim.color("black")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
move =[90,180,270,360]
tim.speed("fastest")
tim.pensize(5)

def movee():
    g = random.choice(move)
    tim.left(g)
    tim.forward(15)
    tim.color(random.choice(colours))

while stop != True:
    movee()

screen = t.Screen()
screen.exitonclick()