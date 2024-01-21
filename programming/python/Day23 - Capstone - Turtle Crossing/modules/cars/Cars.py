from turtle import Turtle
from random import randint

from modules.cars.turtle_colors import colors

class Cars(Turtle):
    def __init__(self, name):
        super().__init__()
        self.car_name = "car" + name
        self.hideturtle()
        self.shape("square")
        self.color(colors[randint(0, len(colors)-1)])
        self.penup()
        self.render = False


    def car_position(self):
        self.x = 300
        self.y = randint(-300, 350)
        self.hideturtle()
        self.position((self.x, self.y))
        # self.sety(self.y)
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)


    def move_car(self):
        self.render_car()
        self.isvisible()
        
        if self.xcor() == 0 and self.ycor() == 0:
            print(f"car: {self.car_name} render: {self.render}")

        elif self.render == True:
            self.showturtle()   
            self.forward(10)
        else:
            self.car_position()

    def render_car(self):
        if randint(1,5) == 1:
            self.render = True
        else:
            self.render = False
    



