'''
    Create a turtle
        w - forwards
        s - backwards
        a - counter clockwise
        d - clockwise
        c - clear and center turtle.
'''

from turtle import Turtle, Screen

def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(5)


def turn_right():
    turtle.right(5)


def clear_window():
    screen.resetscreen()


def set_parameters(turtle, screen):
    turtle.pendown()
    screen.screensize(canvwidth=500, canvheight=500)
    turtle.speed("fastest")
    

def create_objects():
    turtle = Turtle()
    screen = Screen()
    
    return turtle, screen


if __name__ == '__main__':
    turtle, screen = create_objects()
    set_parameters(turtle, screen)
    
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="s", fun=turn_right)
    screen.onkey(key="d", fun=move_backwards)
    screen.onkey(key="c", fun=clear_window)
    screen.exitonclick()