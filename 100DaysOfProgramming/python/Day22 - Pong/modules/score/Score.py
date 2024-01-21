from turtle import Turtle
# from modules.screen.Screen import PongScreen

class ScoreBoard(Turtle):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.playername = name


    def players_score(self):
        return self.p1_score, self.p2_score
    
    def scores(self): 
        if self.playername == "Player 1":

            self.hideturtle()
            self.color("White")
            self.penup()
            self.goto(-40, 350)
            self.write(arg=self.score, move=False, align="center", font=("Consolas", 56, "bold"))
        else:
                self.hideturtle()
                self.penup()
                self.color("White")
                self.goto(40, 350)
                self.write(arg=self.score, move=False, align="center", font=("Consolas", 56, "bold"))

    def add_to_score(self):
        if self.playername == "Player 1":
            self.score += 1
        else:
            self.score += 1
        self.clear()
        self.scores()
