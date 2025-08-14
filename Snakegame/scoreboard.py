



from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("pink")
        self.penup()
        self.goto(x=0, y=270)
        self.speed("fastest")
        self.hideturtle()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Calibre", 14, "bold"))


    def game_over(self):
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=0, y=0)
        self.write("Game Over", False, align="center", font=("Calibre", 14, "bold"))