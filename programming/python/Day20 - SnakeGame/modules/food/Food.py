from turtle import Turtle
from modules.score import Score

class Food(Turtle):
    def __init__(self, x_position, y_position, exists):
        super().__init__()
        self.hideturtle()
        self.x = x_position
        self.y = y_position
        self.exists = exists


    def make_food(self):
        food = Turtle()
        food.setposition (self.x, self.y)
        food.hideturtle()
        food.dot(10, "Blue")
        food.exists = True
        food.penup()

    
    def food_location(self):
        return self.x, self.y
   
   
    def eaten_food(self):
        self.exists = False


    def delete_food(self):
        
        x = self.x
        y = self.y
        food = Turtle()
        food.setposition(x,y)
        food.dot(10,"Black")
        del self
        del food
