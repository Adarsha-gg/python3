from turtle import Screen,distance
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        
    #collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 7:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()