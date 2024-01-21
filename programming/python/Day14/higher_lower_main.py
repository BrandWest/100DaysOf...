from random import randint

from modules import higher_lower_printing
from data import higher_lower_game_data


def choose_celebrity(previous_number2, first):
    if first == True:
        number1 = randint(0, len(higher_lower_game_data.data)-1)
    else: 
        number1 = previous_number2
    
    number2 = randint(0, len(higher_lower_game_data.data)-1)

    while number1 == number2:
        number2 = randint(0, len(higher_lower_game_data.data)-1)
    higher_lower_printing.print_contestents(number1, number2)

    return number1, number2


def comparision(number1, number2, user_choice):
    celebrity_data_1 = int(higher_lower_game_data.data[number1]['follower_count'])
    celebrity_data_2 = int(higher_lower_game_data.data[number2]['follower_count'])

    if celebrity_data_1 > celebrity_data_2 and user_choice == 'a':
        return True
    elif celebrity_data_1 < celebrity_data_2 and user_choice == 'b':
        return True
    elif celebrity_data_1 < celebrity_data_2 and user_choice == 'a':
        return False
    elif celebrity_data_1 > celebrity_data_2 and user_choice == 'b':
        return False
    else: 
        return False


def main():
    total = 0
    playing = True
    first = True
    number2 = ""
    higher_lower_printing.print_logo()
    
    while playing:
        number1, number2 = choose_celebrity(number2, first)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        result = comparision(number1, number2, user_choice)
        
        if result == True:
            total += 1
            higher_lower_printing.print_correct(total)
            first = False
        else:
            playing = False
            higher_lower_printing.print_incorrect(total)


if __name__ == '__main__':
    main()