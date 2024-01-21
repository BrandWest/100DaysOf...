import time
from random import randint

from modules.screen import screen
from modules.snake import snake_body, snake_move
from modules.food.Food import Food
from modules.score.Score import Score


if __name__ == '__main__':
    death = False
    screen = screen.create_screen()
    scoreboard = Score()
    scoreboard.setposition(0,280)
    snakes = snake_body.create_body(0)
    x = randint(-280, 280)
    y = randint(-280, 280)
    food = Food(x, y, True)
    food.make_food()

    while not death:
        scoreboard.write_score()
        time.sleep(.1)
        
        screen.update()
        if not food.exists:
            scoreboard.add_score()
            x = randint(-280, 280)
            y = randint(-280, 280)            
            food = Food(x, y, True)
            food.make_food()
                
        death = snake_move.move_snake_head(snakes, screen, food)
        

    screen.exitonclick()