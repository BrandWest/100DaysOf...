from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, playername, x, max_y, min_y):
        super().__init__()
        self.playername = playername
        self.x = x
        self.max_y = max_y
        self.min_y = min_y
        self.last_hit = False
        self.up = True
        self.down = False

    def draw_paddle(self):
        # self.hideturtle()
        self.penup()
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.x, 0)

    def move_paddle_up(self):
        if not self.ycor() > 400:
            new_y = self.ycor() + 20
            self.sety(new_y)


    def move_paddle_down(self):
        if not self.ycor() < -400:
            new_y = self.ycor() - 30
            self.sety(new_y)

    def move_paddle_two(self):
        barrier = True
        while barrier:
            
            if self.ycor() > -400 and self.down == True:
                self.move_paddle_down()
            elif self.ycor() <= -400 and self.down == True:
                self.down = False
                self.up = True
            elif self.ycor() < 400 and self.up == True:
                self.move_paddle_up()
            elif self.ycor() >= 400 and self.up == True:
                self.up = False
                self.down = True
            barrier = False