from time import sleep

from modules.screen.Screen import PongScreen
from modules.score.Score import ScoreBoard
from modules.paddle.Paddle import Paddle
from modules.ball.Ball import Ball

def main():

    #Objects
    screen = PongScreen()
    player_1 = ScoreBoard("Player 1")
    player_2 = ScoreBoard("Player 2")
    player_1_paddle = Paddle("Player 1", -900, 425, -425)
    player_2_paddle = Paddle("Player 2", 900, 425, -425)
    ball = Ball()
    
    #Attributes/Drawing
    player_1.scores()
    screen.create_field()
    player_2.scores()
    player_1_paddle.draw_paddle()
    player_2_paddle.draw_paddle()
    ball.draw_ball()

    #Variables
    playing = True

    while playing:
        sleep(.01)
        if ball.serve:
            ball.hideturtle()
            ball.goto(0, 0)
            ball.showturtle()
            ball.ball_serve()
        player = ball.ball_move(player_1_paddle,player_2_paddle)

        screen.screen.listen()
        screen.screen.onkey(key="Up", fun=player_1_paddle.move_paddle_up)
        screen.screen.onkey(key="Down", fun=player_1_paddle.move_paddle_down)
        screen.screen.update()
        player_2_paddle.move_paddle_two()

        # print(f"{player_1_paddle.shapesize()}")

        if player == "Player 1":
            player_1.add_to_score()
            ball.serve = True
        elif player == "Player 2":
            player_2.add_to_score()
            ball.serve = True
        
        if player_1.score == 5 or player_2.score == 5:
            playing = False
            
    screen.write("Game Over", "False")


    screen.exitonclick()

if __name__ == "__main__":
    main()