# Imports from Python
import random
import os
#import from created modules
from modules import hangman_art as hma
from modules import hangman_words as hmw

#Variables
word_list = hmw.word_list
display = []
guessed = ""
gameover = False
lives = 6
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
word_length = len(chosen_word)

print("Welcome to \n" + hma.logo)

# set the display to the length of the word
for index in range(word_length):
    display.append("_")

while gameover is False:
	correct = 0
	guess = input("Please guess a letter: ").lower()
	
	if guessed.__contains__(guess):
		print("Letter Guessed Previously. Here are your past guesses\n" + guessed)
	else:
		guessed += guess + " "

	for position in range(word_length):
		letter = chosen_word[position]

		if guess == letter:
			display[position] = guess
			correct = 1
	if correct == 0:
		print(f"The letter '{guess}' is not in the word.")
		lives -= 1
		
	print(f"{' '.join(display)}")
	
	if "_" not in display:
		gameover = True
		print("You Win!")
	
	if lives == 0:
		print(f"You lose. The word was '{chosen_word}'")
		gameover = True
	
	print(hma.stages[lives])
	
