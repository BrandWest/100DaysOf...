import turtle
import pandas as pd
from tkinter import * 

filepath = "/home/caboose/codingProjects/python/udemy/Day25 - CSVs/project/files/blank_states_img.gif"
csv_file = "/home/caboose/codingProjects/python/udemy/Day25 - CSVs/project/files/50_states.csv"


def get_data():
    return pd.read_csv(csv_file)
    

def check_user_guess(data, guess):
    try:
        state_data = data[data.state == guess.title()]

        return state_data 
    except KeyError as e:
        print(f"Key Error: Value {e}")
        return None, None


def write_state(x, y, state):
    state_name = turtle.Turtle()
    state_name.penup()
    state_name.setposition(x.values[0], y.values[0])
    state_name.hideturtle()
    state_name.write(state)


def create_screen():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(filepath)
    turtle.shape(filepath)

    return screen
    

if __name__ == "__main__":
    playing = True
    screen = create_screen()
    data = get_data()

    
    while playing:
        user_guess = screen.textinput("Guess a states name", "Guess the next states name.")
        if user_guess == None:
            playing = False
        else:
            state = check_user_guess(data=data, guess=user_guess)
        
            if not state.x.empty:
                write_state(state.x, state.y, user_guess.title())