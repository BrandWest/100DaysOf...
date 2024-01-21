from turtle import Turtle, Screen
from random import choice, randint

def make_objects():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle_objects = []

    for _ in range(7):
        color = choice(colors)
        turtle = Turtle("turtle")
        turtle.color(color)
        colors.remove(color)
        turtle_objects.append(turtle)

    return turtle_objects

def move_forward(turtles):
    finish = True
    
    for turtle in turtles:
        print(turtle.color())
        if randint(1,2) == 2:
            print("2")
            turtle.forward(randint(0,25))
            finish, turtle = check_finish(turtle)
            if not finish:
                return finish, turtle
       
    return finish, turtles 

    
def check_finish(turtle):
    print(turtle.xcor())
    if turtle.xcor() > 500:
        return False, turtle
    else:
        return True, turtle
 

def print_winner(turtle, user_guess):
    print(f"The {turtle.color()[0]} turtle won the race! Your guess was: {user_guess}.")


def popup():
    return screen.textinput("Which turtle will win?", "red, orange, yellow, green, blue, indigo, violet")


def set_positions(turtles):
    x = -240
    y = -150
    for turtle in turtles:
        turtle.penup()
        turtle.setheading(0)
        turtle.setposition(x, y)
        turtle.setposition(x, y)
        y += 50


def race(turtles):
    racing, turtle = move_forward(turtles)

    return turtle, racing

    
if __name__ == '__main__':
    screen = Screen()
    racing = True
    screen.setup(height=400, width=1000)
    users_guess = popup()
    turtle_objects = make_objects()
    set_positions(turtle_objects)
    while racing:
        turtle, racing = race(turtle_objects)
        print(racing)
    print_winner(turtle, users_guess)
    screen.exitonclick()
