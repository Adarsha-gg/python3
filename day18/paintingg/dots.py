import turtle as t 
import colorgram
import random

# colors = colorgram.extract("cd.jpg", 10)
# rgb =[]
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new = (r, g, b)
#     rgb.append(new)
#print(rgb)          
color_list = [(227, 231, 235), (58, 106, 147), (225, 201, 110), (133, 82, 58), (223, 136, 61), (196, 145, 171), (235, 226, 203), (223, 233, 229), (143, 179, 203), (139, 82, 
105)]

tim = t.Turtle()
t.colormode(255)
tim.up()
minus = 0
tim.speed("fastest")
def draw(minus):
    for space in range (10):
        tim.setx(-300 )
        tim.sety(-300 + minus)
        minus += 50
        for i in range(10):
        
            tim.dot(20,random.choice(color_list))
            tim.forward(50)
    tim.hideturtle()        
        

draw(minus)



screen = t.Screen()
screen.exitonclick()