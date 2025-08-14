
from turtle import Turtle
Up=90
Down=270
Left=180
Right=0

class Snake:



    def __init__(self):

        x = 0
        self.timmy = []
        for i in range(3):
            turtle = Turtle("square")
            turtle.color('white')
            turtle.penup()
            turtle.goto(x, 0)
            self.timmy.append(turtle)
            x -= 20
        self.head = self.timmy[0]

    def extend(self):
        last = self.timmy[-1]
        new = Turtle("square")
        new.color('white')
        new.penup()
        new.goto(last.position())
        self.timmy.append(new)
    def move(self):
        for turtle_no in range(len(self.timmy)- 1, 0, -1):
            x_axis=self.timmy[turtle_no-1].xcor()
            y_axis=self.timmy[turtle_no-1].ycor()
            self.timmy[turtle_no].goto(x_axis,y_axis)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)


    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)


    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)


