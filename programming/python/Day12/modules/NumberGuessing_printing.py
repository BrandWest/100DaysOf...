def difficulty_selection(decision, guesses_remaining):
    if decision == 'easy':
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
    else:
        print(f"You have {guesses_remaining} attempts remanining to guess the number.")

def make_a_guess():
    return input("Make a guess: ")

def print_result(value, answer, guesses_remaining):
    if value == "high":
        print(f"Too High!\nYou have {guesses_remaining} attempts remanining to guess the number.")
    elif value == "low":
        print(f"Too Low!\nYou have {guesses_remaining} attempts remanining to guess the number.")
    elif value == "win":
        print_winner(answer)


def print_winner(answer):
    print(f"You got it! The answer was {answer}")

def print_loser(answer):
    print(f"You were unable to get the answer of {answer}")