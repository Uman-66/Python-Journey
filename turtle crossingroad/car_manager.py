import random

from turtle import Turtle
COLORS=["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE=5


class CarMmanager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.MOVE_INCREMENT = 10


    def create_cars(self):
        chance=random.randint(0,3)
        if chance==1:
            new_car=Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y=random.randint(-280,280)
            new_car.goto(x=280, y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            x_term = car.xcor()
            y_term = car.ycor()
            x_term = x_term - self.MOVE_INCREMENT
            car.goto(x_term, y_term)
