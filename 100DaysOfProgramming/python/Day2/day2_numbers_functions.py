#TypeError: You can only concatenate strings not ints
num_char = len(input("what is your name? "))
print("Your name has " + str(num_char) + " characters.")


'''
Type Fucntions
	Checking the type() of a datatype
'''

'''
Type Casting
	str(variable)
    int(variable)
	Changing the tyupes of data types
'''

a = 123
print(type(a))
print(type(str(a)))
print(type(float(str(int(a)))))



number = input("Insert two digit number: ")
num1 = number[0]
num2 = number[1]

print(int(num1) + int(num2))