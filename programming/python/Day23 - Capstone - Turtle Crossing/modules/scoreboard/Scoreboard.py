from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, name):
        super().__init__()
        self.score = 0
