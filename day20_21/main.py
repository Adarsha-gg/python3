import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")

screen.title("SNAKE")
screen.tracer(0)


snake = Snake()

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
    


screen.exitonclick()