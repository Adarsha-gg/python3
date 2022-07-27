import turtle
import time
from level import Level
from player import Player
from cars import Car


screen = turtle.Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")

player = Player()
level = Level()
car = Car()

Game_on = True
screen.tracer(0)


screen.listen()
screen.onkey(key = "Up", fun = player.up)

while Game_on:
    time.sleep(0.1)
    screen.update()
    car.generate()
    car.move()
        

    #detect collision
    for carr in car.all_car:
        if carr.distance(player) < 20:
            Game_on = False
            level.over()

    if player.is_at_finish_line():
        level.increase()    
        car.level_up()
        player.go_to_start()


screen.exitonclick()