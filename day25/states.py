from email.errors import MissingHeaderBodySeparatorDefect
import turtle
import pandas

screen = turtle.Screen()
screen.title("Welcome to State guessing game")
image = "day25\ez.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("day25/all_states.csv")
total_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    ans = screen.textinput(title="Guess the state",prompt="What is the name of the state").title()

    if ans == "Exit":
        missing = [state for state in total_states if state not in guessed_states]
        new = pandas.DataFrame(missing)
        new.to_csv("day25/Missed")        

        break 

    if ans in total_states:
        hero = data[data.state == ans]
        
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(hero.x),int(hero.y))
        tim.write(ans)
        guessed_states.append(hero)



 