from turtle import Turtle, Screen
import random
from colour import colors

timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new= (r, g, b)
    return new
# angles=[120,90,72,60,51.4285714,45,40,36]
# timmy.color(random.choice(colors))
# angle_shape = 0
# sides = 3
# for shape in range (9):
#     timmy.color(random.choice(colors))
#     timmy.shape("turtle")
#     for i in range(sides):
#        timmy.forward(100)
#        timmy.right(angles[angle_shape])
#     angle_shape += 1
#     sides += 1
#
#

# start= True
#
# while start:
#
#     random_color()
#
#     timmy.color(random_color())
#     turn= random.choice([90, 180, 270, 360])
#     timmy.setheading(turn)
#     timmy.forward(10)

n=0
for i in range(0,360):
    color = random_color()
    timmy.color(color)
    timmy.setheading(i)
    timmy.circle(100)
    n+=5


screen.exitonclick()

