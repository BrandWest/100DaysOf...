from turtle import Turtle

def create_body(food):
    snake_objects = []
    for _ in range(food+3):
        snake = Turtle()
        set_color(snake)
        set_shape(snake)
        set_pen_position(snake)
        snake_objects.append(snake)
    starting_position(snake_objects)

    return snake_objects

def set_color(snake):
    snake.color("white")


def set_shape(snake):
    snake.shape("square")


def starting_position(snakes):
    x = 0
    y = 0
    for snake in snakes:
        snake.setposition(x,y)
        x -= 20

def add_len(snakes):
    snake = Turtle()
    set_color(snake)
    set_shape(snake)
    set_pen_position(snake)
    snakes.append(snake)

def set_pen_position(snake):
    snake.penup()