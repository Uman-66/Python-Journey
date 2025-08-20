

from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def start(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-210, 250)
        self.write(f"Level = {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.start()
    def over(self):
        self.goto(0, 0)
        self.write("Game Over, You hit a car", align="center", font=FONT)