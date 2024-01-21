from turtle import Screen


def create_screen():
    screen = Screen()
    set_height_width(screen)
    set_background(screen)
    set_title(screen)
    screen.tracer(0)

    return screen

def set_height_width(screen):
    screen.setup(width=600, height=600)

def set_background(screen):
    screen.bgcolor("black")

def set_title(screen):
    screen.title("Snake")