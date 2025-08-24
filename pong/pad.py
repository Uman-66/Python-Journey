from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, ):
        self.y = 0
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)


    def position(self, x_position):
        self.goto(x_position, 0)


    def go_up(self):
        x=self.xcor()
        self.y += 40
        self.goto(x, y=self.y)

    def go_down(self):
        x=self.xcor()

        self.y -= 20
        self.goto(x,y=self.y)