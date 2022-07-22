import turtle as t 
import random
class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5) #len half and widhth half    
        self.color("green")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)