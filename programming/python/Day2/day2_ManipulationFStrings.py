'''# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
age_until_90 = 90 - int_age
days = age_until_90 * 365
weeks = age_until_90  * 52
months = age_until_90 * 12


print(f"You have {days} days, {weeks} weeks, and {months} months left.")'''
'''
Tip calculator
What was the total bill? $124.56
What percentage tip? 10, 12, 15
how many people splitting the bill?
Each person should pay: $
'''

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage would tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

split_bill = round( ((total_bill * ( tip_amount / 100 ) + total_bill)  / num_people), 2)

print(f"Each person should pay: ${split_bill:.2f}")