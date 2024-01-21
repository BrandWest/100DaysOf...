# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_counter = 0
love_counter = 0
total = 0

for letter in name1:
	letter = letter.upper()
	if letter == "L" or letter == "O" or letter == "V" or letter == "E":
		love_counter += 1
	if letter == "T" or letter == "R" or letter == "U" or letter == "E":
		true_counter += 1
	
for letter in name2:
	letter = letter.upper()
	if letter == "L" or letter == "O" or letter == "V" or letter == "E":
		love_counter += 1
	if letter == "T" or letter == "R" or letter == "U" or letter == "E":
		true_counter += 1

	total = str(true_counter) + str(love_counter)
	total = int(total)

if total < 10 or total > 90:
	print(f"Your score is **{total}**, you go together like coke and mentos.")

elif total >= 40 and total <= 50:
	print(f"Your score is **{total}**, you are alright together.")
else: 
	print(f"Your score is **{total}**.")