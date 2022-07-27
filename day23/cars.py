import turtle
import random
COLORS = ["red","green","yellow","blue","purple","orange"]
Move = 5
INCREMENT = 10

class Car(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.all_car = []
        self.car_speed = Move

    def generate(self):
        random_chance = random.randint(2,6)
        if random_chance == 6:
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-270,270)
            new_car.goto(270,new_y)
            self.all_car.append(new_car)

      
    def move(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT
        