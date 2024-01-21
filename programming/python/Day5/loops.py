'''
Loops
	for loops
		for item in list_of_items:
			Do something.
			#In for loop
		#out of for loop
		Each iteration gets something to do.
'''

fruits = ["Aple", "Peach", "Pear"]
for fruit in fruits:
	print(fruit)
	print(fruit + " pie")
	print(fruits)
print(fruits)

'''
Loops + Range
	for number in range(a, b):
		print(number)
'''
#1-9
for number in range(1, 10):
	print(number)
#1-10
for number in range(1, 11):
	print(number)

total = 0
for number in range(1, 101):
	total += number
print(total)