from turtle import _Screen, TurtleScreen, Turtle
from modules.scoreboard.Scoreboard import Scoreboard

class PlayArea(_Screen):
    def __init__(self):
        super().__init__()
        TurtleScreen.__init__(self, PlayArea._canvas)
        if Turtle._screen is None:
            Turtle._screen = self
        self.setup(width=900, height=800, startx=None, starty=None)
        self.title("Turtle Crossing")
        self.bgcolor("Grey")
        
        # self.tracer(0)

    def show_score(self):
        self.write

    
    def click_exit(self):
        self.exitonclick()