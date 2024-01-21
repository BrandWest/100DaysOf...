from random import randint
from turtle import Turtle

from modules.score.Score import ScoreBoard

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_min = -450
        self.y_min = -425
        self.x_max = 450
        self.y_max = 425
        self.serve = True
        self.wall = False
        self.paddle = False
        self.angle = 0

    def draw_ball(self):
        self.color("White")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)

    def ball_position(self):
        return self.xcor(), self.ycor()

    def ball_move(self, paddle1, paddle2):
        if self.distance(self.xcor(), self.y_max) < 15:
            self.wall = True
            self.ball_collission_wall()
        elif self.distance(self.xcor(), self.y_min) < 15:
            self.wall = True
            self.ball_collission_wall()            
        else:
            self.forward(10)

        if self.distance(paddle1.position()) <= 40:
            self.ball_collission_paddle()
        elif self.distance(paddle2.position()) <= 40:
            self.ball_collission_paddle()
        else:
            pass
        
        scored, player = self.ball_past_paddle()
        if scored == True:
            return player

    def collission(self):
        reflective_angle = 360 - self.heading()
        if reflective_angle + 180 == 360:
            reflective_angle = randint(0,360)
            return reflective_angle
        elif reflective_angle < 0:
            reflective_angle *= -1
            return reflective_angle
        else:
            return reflective_angle

    def ball_collission_wall(self):
        self.setheading(self.collission())
        self.forward(25)
        self.wall = False

    def ball_collission_paddle(self):
        heading = 180 - self.heading()
        if heading < 0:
            heading *= -1
        self.setheading(heading)
        self.forward(25)
        self.wall = False


    def ball_past_paddle(self):
        if self.xcor() < -920:
            return True, "Player 2"
        elif self.xcor() > 920:
            return True, "Player 1"
        return False, None

    def ball_serve(self):
        direction = randint(75, 255)
        self.angle = direction
        self.setheading(direction)
        self.serve = False