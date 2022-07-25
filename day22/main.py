import imp
from turtle import Screen,Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboardd import Scoreboard

game_on = True
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun = r_paddle.up)
screen.onkey(key = "Down", fun = r_paddle.down)
screen.onkey(key = "w", fun = l_paddle.up)
screen.onkey(key = "s", fun = l_paddle.down)

while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    scoreboard
    #detect collison wiht upper and lower walls
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide()
        

    #detect collision with right paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 340:
        ball.collidepaddle()
        ball.hard()

    #detect collision with right paddle
    if ball.distance(l_paddle) < 40 and ball.xcor() < -340:
        ball.collidepaddle()
        ball.hard()
        
    #detect miss (left)
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_add()

    #detect miss (right)    
    if ball.xcor() > 380:
        ball.reset()    
        scoreboard.l_add()

screen.exitonclick()