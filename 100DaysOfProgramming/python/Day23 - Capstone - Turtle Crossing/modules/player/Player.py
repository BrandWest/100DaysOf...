from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.hideturtle()
        self.penup()
        self.showturtle()
        self.goto(0, -350)
        self.color("Black")
        self.setheading(90)

        

    # def create_player(self):
        # print(f"{ self.shape()}, {self.xcor()}, {self.ycor()}")

    def move_forward(self):
        pass
    
    
    def finish(self):
        pass


    def player_reset(self):
        pass


    def player_dies(self):
        pass