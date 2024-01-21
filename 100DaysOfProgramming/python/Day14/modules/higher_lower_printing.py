from modules import higher_lower_art
from data import higher_lower_game_data
import os 


def print_logo():
    print(higher_lower_art.logo)

def print_contestents(number1, number2):
    print(f"Compare A: {higher_lower_game_data.data[number1]['name']} a {higher_lower_game_data.data[number1]['description']} from {higher_lower_game_data.data[number2]['country']}.")
    print(higher_lower_art.vs)
    print(f"Against B: {higher_lower_game_data.data[number2]['name']} a {higher_lower_game_data.data[number2]['description']} from {higher_lower_game_data.data[number2]['country']}.")

def print_correct(total_correct):
    os.system('clear')
    print_logo()
    print(f"You're right! Current score: {total_correct}")

def print_incorrect(total_correct):
    os.system('clear')
    print_logo()
    print(f"Sorry, that's wrong. Final score: {total_correct}")