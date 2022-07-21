import turtle as t
import random

game_on = False
screen = t.Screen()
screen.setup(width = 500,height = 500)
guess = screen.textinput(title = "Winner",prompt = "Who is going too win?:")
colors = ["red", "blue", "purple", "green", "orange",]

turtles = []
major = 0
for i in range(5):
    new_turtle = t.Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.goto(-235,-200 + major)
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    major += 100

if guess:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 215:
            game_on = False
            winner = turtle.pencolor()
            if guess == winner:
                print(f"You've won the winner turtle is {winner}")
            else:
                print(f"You've lost the winner turtle is {winner}")    
        distance = random.randint(0,10)
        turtle.forward(distance)



screen.exitonclick()