from score import Score
from turtle import Screen
from  pad import Paddle
from ball import Ball
import time
screen = Screen()
screen.bgcolor("black")
pad1=Paddle()
pad1.position(-350)
pad2=Paddle()
pad2.position(350)
ball= Ball()
screen.tracer(0)
score_board = Score()
screen.setup(width=800, height=600)
screen.listen()

screen.onkey(pad2.go_up, "Up")
screen.onkey(pad2.go_down, "Down")
screen.onkey(pad1.go_up, "w")
screen.onkey(pad1.go_down, "s")
game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad2) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(pad1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380 :
        ball.reset_ball()
        score_board.l_win()
    if ball.xcor() < -380:
        ball.reset_ball()
        score_board.r_win()
screen.exitonclick()
