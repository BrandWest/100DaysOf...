'''
if condition:
	do this
else:
	do that
    
nested:

if condition:
	if condition:
		do this
    else:
		do this
else: 
	do this
'''


'''
Multi conditional chekcks
'''


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
ticket = input("Do you want a photo? Y or N. ")
bill = 0


if height >= 120:
    if age > 18:
        print("You can ride, audlt rides cost $12.")
        bill = 12
    elif age < 12:
        print("You can ride, children rides cost $5.")
        bill = 5
    else:
        print("You can ride, youth rides cost $7.")
        bill = 7
    
	#Adds a bill cost to it
    if ticket == "Y":
        bill += 3

else:
    print("You can not ride to rollercoaster.")


print(f"Your total is: ${bill}.")





