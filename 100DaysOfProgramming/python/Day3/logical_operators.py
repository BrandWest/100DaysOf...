'''
Logical Operators
	Mulitple conditions in the same line of code
    if condition1 & condition2 & condition 3
    
    AND if condition1 AND condition2 is true 
    OR if condition1 OR condition2 is true 
    NOT if condition1 NOT condition2 is true 
'''


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
ticket = input("Do you want a photo? Y or N. ")
bill = 0


if height >= 120:
    if age > 18 and age < 45:
        print("You can ride, audlt rides cost $12.")
        bill = 12
    elif age < 12:
        print("You can ride, children rides cost $5.")
        bill = 5
    elif age >= 45 or age <= 55:
        print("You can ride for free")
        bill = 0
    else:
        print("You can ride, youth rides cost $7.")
        bill = 7
    
	#Adds a bill cost to it
    if ticket == "Y":
        bill += 3

else:
    print("You can not ride to rollercoaster.")


print(f"Your total is: ${bill}.")
