from modules import turtle_module
print(turtle_module.variable)

from turtle import Turtle, Screen

#timmy = turtle.Turtle()
timmy = Turtle()
print(timmy)

#objects
screen = Screen()
#attributes
height = screen.canvheight
width = screen.canvwidth

print(height, width)

'''
Methods
'''
#function notation timmy.method()
#change the shpae of the cursor
timmy.shape("turtle")
#Change the color
timmy.color("DeepPink")
#move forward   
timmy.forward(100)

screen.exitonclick()

