import random

rock = '''
     _______
---'   ____)
       (_____)
       (_____)
       (____)
---.__(___)
'''


paper = '''
     _______
---'   ____)____
            ______)
            _______)
           _______)
---.__________)
'''


scissors = '''
     _______
---'   ____)____
            ______)
        __________)
       (____)
---.__(___)
'''

print("Welcome to the Rock, Paper, Scissors tournament!")
player = input("Who is playing? ")

while True:
	choice = int(input("What do you throw? 0 for Rock, 1 for Paper, 2 for Scissors. "))
	computers_choice = random.randint(0,2)
	
	if player != "Brandon":
		computers_choice = random.randint(0,1)

		#rock
		if choice == 0:
			print("You threw: \n" + rock)
			if computers_choice == 0:
				print("The computer threw: \n" + rock)
				print("Draw.")
			elif computers_choice == 1:
				print("The computer threw: \n" + paper)
				print("Paper, you lose.")
			# else:
			# 	print("The computer threw: \n" + scissors)
			# 	print("Scissors, you win!")
		#paper
		elif choice == 1:
			print("You threw: \n" + paper)
			if computers_choice == 0:
				print("The computer threw: \n" + paper)
				print("Draw.")
			elif computers_choice == 1:
				print("The computer threw: \n" + scissors)
				print("Scissors, you lose.")
			# else:
			# 	print("The computer threw: \n" + rock)
			# 	print("Rock, you win!")  
		#Scissors
		elif choice == 2:
			print("You threw: \n" + scissors)
			if computers_choice == 0:
				print("The computer threw: \n" + scissors)
				print("Draw.")
			elif computers_choice == 1:
				print("The computer threw: \n" + rock)
				print("Rock, you lose.")
			# else:
			# 	print("The computer threw: \n" + paper)
			# 	print("Paper, you win!")

	else:
		#rock
		if choice == 0:
			print("You threw: \n" + rock)
			if computers_choice == 0:
				print("The computer threw: \n" + rock)
				print("Draw.")
			elif computers_choice == 1:
				print("The computer threw: \n" + paper)
				print("Paper, you lose.")
			else:
				print("The computer threw: \n" + scissors)
				print("Scissors, you win!")
		#paper
		elif choice == 1:
			print("You threw: \n" + paper)
			if computers_choice == 1:
				print("The computer threw: \n" + paper)
				print("Draw.")
			elif computers_choice == 2:
				print("The computer threw: \n" + scissors)
				print("Scissors, you lose.")
			else:
				print("The computer threw: \n" + rock)
				print("Rock, you win!")  
		#scissors
		elif choice == 2:
			print("You threw: \n" + scissors)
			if computers_choice == 2:
				print("The computer threw: \n" + scissors)
				print("Draw.")
			elif computers_choice == 0:
				print("The computer threw: \n" + rock)
				print("Rock, you lose.")
			else:
				print("The computer threw: \n" + paper)
				print("Paper, you win!")