from turtle import Screen,Turtle
import time

from paddle import Paddle



screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PONG")

paddle1 = Paddle()
screen.listen()
screen.onkey(key = "Up", fun = paddle1.up)
screen.onkey(key = "Down", fun = paddle1.down)
screen.onkey(key = "Left", fun = paddle1.left)
screen.onkey(key = "Right", fun = paddle1.right)




















screen.exitonclick()