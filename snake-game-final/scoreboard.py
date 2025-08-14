from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# C:\Users\uSER\Desktop
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("C:/Users/uSER/Desktop/data.txt", mode="r")
        self.highscore = int(file.read())
        self.score = 0
        file.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    # C:\Users\uSER\Desktop
    def game_reset(self):
        if self.score > self.highscore:
            file = open("data.txt", mode="w")
            file.write(str(self.score))
            self.highscore = self.score
            file.close()
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
