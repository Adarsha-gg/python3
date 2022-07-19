from turtle import Screen, Turtle
import random


tim = Turtle()
tim.shape("arrow")
tim.color("black")
sides = 3
while sides < 10:
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    #The rgb feature didnt work sadly F
    for i in range(sides):
        tim.right(360/sides)
        tim.forward(50)

    sides += 1

while sides != 2:
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    #The rgb feature didnt work sadly F
    for i in range(sides):
        tim.right(360/sides)
        tim.backward(50)

    sides -= 1
    
tim.left(180)
tim.forward(200)

while sides != 10:
    
    #The rgb feature didnt work sadly F
    for i in range(sides):
        tim.right(360/sides)
        tim.backward(50)

    sides += 1    
screen = Screen()
screen.exitonclick()