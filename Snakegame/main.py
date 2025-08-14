from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
screen = Screen()
screen.listen()
snake = Snake()
food = Food()



screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on=True
scoreboard = ScoreBoard()
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False

    listen = snake.timmy[1::]

    for segment in listen:
        if snake.head.distance(segment) < 15:
            game_on = False


scoreboard.game_over()


screen.exitonclick()