from turtle import Turtle

# from modules.food.Food import Food
from . import snake_body


def move_snake_head(snakes, screen, food):
    positions = get_positions(snakes)
    snake_head = snakes[0]
    distance = snake_head.distance(food.x, food.y)
    
    if round(distance) <= 15 :
        food.eaten_food()
        food.delete_food()
        snake_body.add_len(snakes)


    def move_forward(snakes, positions):
        index = 0
        for snake in snakes:
            snake.goto(positions[index])
            index += 1


    def move_east():
        if snake_head.heading() != 180:
            snake_head.setheading(0)


    def move_north():
        if snake_head.heading() != 270:
            snake_head.setheading(90)


    def move_south():
        if snake_head.heading() != 90:
            snake_head.setheading(270)



    def move_west():
        if snake_head.heading() != 0:
            snake_head.setheading(180)    

        
    screen.listen()
    screen.onkey(key="Up", fun=move_north)
    screen.onkey(key="Left", fun=move_west)
    screen.onkey(key="Right", fun=move_east)
    screen.onkey(key="Down", fun=move_south)

    snake_head.forward(20)
    
    if snake_check_position(snake_head, positions):
        return True
    else:    
        move_forward(snakes[1:], positions)
        return False

    
def snake_check_position(snake_head, positions):
    if snake_head.xcor() > 300 or snake_head.xcor() < -300:
        return True
    elif snake_head.ycor() > 300 or snake_head.ycor() < -300:
        return True
    elif snake_body_collision(snake_head, positions):
        return True
    else:
        return False


def snake_body_collision(snake_head, positions):
    for position in positions:
        print(snake_head.position(), position)
        if snake_head.position() == position:
            return True
    return False


def get_positions(snakes):
    positions = []
    for snake in snakes:
        positions.append(snake.position())
    return positions
