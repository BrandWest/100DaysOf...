from random import randint

from modules import NumberGuessing_printing

def play(difficulty):
    continue_playing = True

    while continue_playing == True:
        if difficulty == 'easy':
            guesses_remaining = 10
        elif difficulty == 'hard':
            guesses_remaining = 5
        
        number = get_number()
        NumberGuessing_printing.difficulty_selection(difficulty, guesses_remaining)
        
        for i in range(guesses_remaining):
            guesses_remaining -= 1
            guessed_number = NumberGuessing_printing.make_a_guess()
            next_guess = compare(answer=number, guess=int(guessed_number), guesses_remaining=guesses_remaining)
            if next_guess == 0:
                NumberGuessing_printing.print_loser(number)
                break
            elif next_guess == 2:
                NumberGuessing_printing.print_loser(number)
        # response = 
        # print(response)
        if input("Do you want to play again? Y/N ").lower() == "n":
            # print(response)
            continue_playing = False
            print("Thank you for playing!")

            
def compare(answer, guess, guesses_remaining):
    if guess > answer and guesses_remaining != 0:
        NumberGuessing_printing.print_result("high", answer=answer, guesses_remaining=guesses_remaining)
        return 1
    elif guess < answer and guesses_remaining != 0:
        NumberGuessing_printing.print_result("low", answer=answer, guesses_remaining=guesses_remaining)
        return 1
    elif guess == answer and guesses_remaining != 0:
        NumberGuessing_printing.print_result("win", answer=answer, guesses_remaining=guesses_remaining)
        return 0

    elif guesses_remaining == 0:
        return 2

def get_number():
    return randint(1, 101)

    