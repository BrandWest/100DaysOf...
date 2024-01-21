from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.total = 0

    def add_score(self):
        self.clear()
        self.total += 1

    def write_score(self):
        self.pencolor("White")
        self.penup()
        self.write(arg=f"Score: {self.total}", move=False, align="Center")
        