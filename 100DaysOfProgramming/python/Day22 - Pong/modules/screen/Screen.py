from turtle import Turtle, Screen

from modules.score.Score import ScoreBoard

class PongScreen(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.setup(width=2000, height=900, startx=None, starty=None)
        screen.title("P O N G")
        screen.bgcolor("Black")
        screen.tracer(0)

    
    def create_field(self):
       dashed_line_writer = Turtle()
       dashed_line_writer.color("White")
       dashed_line_writer.speed("fastest")
       dashed_line_writer.pencolor("White")
       dashed_line_writer.pensize(5)
       dashed_line_writer.penup()
       dashed_line_writer.goto(0,435)
       dashed_line_writer.setheading(270)
       dashed_line_writer.hideturtle()
       for _ in range(28):
            dashed_line_writer.penup()
            dashed_line_writer.forward(15)
            dashed_line_writer.pendown()
            dashed_line_writer.forward(15)

    def exitonclick(self):
        self.screen.exitonclick()

    
