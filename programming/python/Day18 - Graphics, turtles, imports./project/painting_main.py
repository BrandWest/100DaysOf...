'''
    Colorgram - extract colors from images
    10 x 10 dots
    20 in size
    50 paces spread out
'''
import colorgram as cg
from turtle import Turtle, Screen
from random import randint


def create_screen(width, height):
    timmy = Turtle()
    screen = Screen()
    screen.setup(width=width, height=height)

    return timmy, screen

def set_paramters(timmy, screen):
    screen.colormode(255)
    timmy.pensize(20)

def calculate_start_position(number_of_dots, window_height, window_width):
    startx = ((window_height - 50) * -1)
    starty = ((window_width - 50) * -1)
    total_dots = number_of_dots * number_of_dots

    return startx, starty, total_dots

def set_color(color):
    timmy.color(color)
    timmy.pencolor(color)


def paint_dot(color_codes, spread, startx, starty):
    next_dot = True
    dots = 0
                
    while next_dot:
        if dots % 10 == 0 and dots != 100:
            timmy.penup()
            starty = starty + 50
            timmy.setpos((startx + 50), starty)
            timmy.forward(spread)
            timmy.pendown()
            timmy.forward(0)
            
        elif dots % 10 != 0:
            color = randint(0, len(color_codes)-1)
            set_color(color_codes[color])
            timmy.penup()
            timmy.forward(spread)
            timmy.pendown()
            timmy.forward(0)
        elif dots == 100:      
            next_dot = False

        dots += 1

def move_turtle(spread):
    timmy.forward(spread)

def exit_program(screen):
    screen.exitonclick()

def extract_colors(file_path, number_of_colors):
    return cg.extract(file_path, number_of_colors)

def create_color_tuple(color_object):
    color_codes = []
    for color in color_object:
        color_codes.append((color.rgb.r,color.rgb.g,color.rgb.b))

    return color_codes

if __name__ == '__main__':
    file_path = r"/home/caboose/codingProjects/python/udemy/Day18/project/painting/valium_spot_painting.png"
    number_of_colors = 100
    spread = 50
    width = 550
    height = 650
    size = 20
    number_of_dots = 5
    # color_object = extract_colors(file_path, number_of_colors)
    # color_codes = create_color_tuple(color_object)
    color_codes = [(224, 220, 222), (224, 220, 215), (218, 221, 225), (204, 161, 114), (219, 223, 221), (150, 87, 52), 
                   (142, 169, 183), (42, 105, 133), (204, 153, 21), (147, 18, 56), (220, 200, 139), (194, 148, 160), 
                   (19, 49, 72), (144, 67, 85), (60, 39, 32), (141, 169, 156), (62, 31, 50), (194, 100, 76), (67, 110, 84), 
                   (186, 91, 114), (10, 59, 50), (6, 83, 110), (110, 43, 34), (218, 176, 187), (216, 180, 173), (13, 91, 75), 
                   (76, 149, 166), (171, 199, 207), (95, 73, 21), (183, 191, 203)] 
    timmy, screen = create_screen(width=width, height=height)
    set_paramters(timmy, screen)
    # startx, starty, total_dots = calculate_start_position(number_of_dots, screen.window_height(), screen.window_width())
    # print(startx, starty)
    paint_dot(color_codes, spread, -350, -350)
    exit_program(screen)
    
    