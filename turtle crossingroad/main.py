import time
from turtle import Screen

from car_manager import CarMmanager
from player import Player
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car=CarMmanager()
turtle = Player()
screen.listen()
scoreboard.start()
screen.onkey(turtle.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for loop_car in car.all_cars:
        if turtle.distance(loop_car) < 20:
            game_is_on = False
            scoreboard.over()
    if turtle.reached_end():
        turtle.go_to_start()
        scoreboard.increase_score()
screen.exitonclick()