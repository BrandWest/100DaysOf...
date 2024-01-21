'''
    tkinter = tk interface GUI

    How to import modules
    keyword modulename
    
    Basic:
        import turtle
        timmy = turtle.Turtle()
    
    intermediate
        from turtle import Turtle
        timmy = Turtle()

    advance (not good)
        from turtle import *
    
    aliasing modules
        from turtle import Turtle as t

    Installing modules
        pip install module_name 
'''
from turtle import Turtle, Screen
from random import randint 

if __name__ == '__main__':
    timmy = Turtle()
    timmy.shape("turtle")
    screen = Screen()
    #Is required for the color
    screen.colormode(255)
    #make a squre
    # for _ in range(4):
    #     timmy.forward(100)
    #     timmy.right(90)
    
    #Make a dashed line
    # for _ in range(50):
    #     timmy.forward(5)
    #     timmy.penup()
    #     timmy.forward(5)
    #     timmy.pendown()
'''
    tuples
        data type in python
        (#1, #2, #2) <- this is an example of a touple which are ordered
            cant be modified.
            cant be changed in anyway. "Carved in stone" Immutable.
            list(tuple) will allow reassignment.
        [#3, #1, #3] <- a list
'''

'''
    triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
    random colors
'''
def sided_shape():
    index = 3
    next_shape = True
    while next_shape == True:
        r,g,b = random_color()
        set_color(r,g,b)

        angle = 360 / index
        draw_shape(index, angle)

        index += 1
        if index > 10:
            next_shape = False


def set_color(r,g,b):
    timmy.color(r,g,b)
    timmy.pencolor(r,g,b)
    

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return r,g,b

def spirograph():
    size = 100
    timmy.speed(0)
    size_of_graph = 2
    # timmy.circle(size/2)
    for _ in range(int(360/size_of_graph)):
        timmy.right(size_of_graph)
        timmy.circle(size, None, 100)
        r,g,b = random_color()
        set_color(r,g,b)



def paint_direction(direction):
    east = 0
    north = 90
    west = 180
    south = 270

    if direction == 0:
        timmy.setheading(east)
    elif direction == 1:
        timmy.setheading(north)
    elif direction == 2:
        timmy.setheading(west)
    elif direction == 3:
        timmy.setheading(south)


def move_turtle(amount):
    timmy.forward(amount)


def random_walk():
    timmy.pensize(10)
    timmy.speed(0)
    for _ in range(0,1000):
        direction = randint(0,3)
        paint_direction(direction)
        r,g,b = random_color()
        set_color(r,g,b)
        move_turtle(20)


def draw_shape(index, angle):
    for _ in range(index):    
        timmy.forward(100)
        timmy.left(angle)
    
    
if __name__ == "__main__":
    # sided_shape()
    # random_walk()
    spirograph()
    #End function
    screen.exitonclick()