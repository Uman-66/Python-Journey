from turtle import Turtle, Screen
import random

start = False
screen = Screen()
screen.setup(width=500, height=400)
guess=screen.textinput(title="Guess who will win?", prompt="Choose any colour from yhe rainbow")

color=["purple", "blue", "green", "yellow", "orange", "red"]
timmy= []
color_index=0
position = -150
for  new in range(6):
    turtle=Turtle(shape="turtle")
    turtle.color(color[color_index])
    color_index += 1
    turtle.penup()
    turtle.goto(x=-230, y=position)
    position += 60
    timmy.append(turtle)


if guess:
    start=True


while start:


    for turtle in timmy:
        if turtle.xcor() > 230:
            wining_color=turtle.pencolor()
            if wining_color == guess:
                print(f"Congratulations you won! {wining_color} won the race")
            else:
                print(f"Sorry, you loose, {wining_color} won the race")
            start = False
        number=random.randint(1,10)
        turtle.forward(number)



screen.exitonclick()
