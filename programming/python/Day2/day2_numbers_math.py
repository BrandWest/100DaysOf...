'''
Add 		3 + 5
Minus 		5 - 2
Multi		7 * 4
Division	8 / 2 <--- will always get a float. We can change it to an int
Exponets	2 ** 2

Precedence
	PEMDAS 
		()
        **
        */
        +-
        
    Whatever is most to the left will be done first.
'''

print(3 * 3 + 3 / 3 - 3) # = 7
print(3 / 3 * 3 - 3 + 3) # = 3


# 3/3 = 1
# 3*1 =3
# 3-3 = 0
# 3 + 0 = 3

'''
Floor division
	// 
    Used when dividing and removing everything after the decimal
'''
print( 8 // 3) # Will give you the removed data. 
print( 8 / 3 )
print(round(8 / 3))

result = 4 / 2 	# = 2 
result /= 2 	# Similar to +=. *=, -=
print(result)

''' 
F strings
	Mixing strings and data types
'''
score = 0
height = 1.8
winning = True

#Can mix and match without the str() function requirement.
print( f"your score is {score}, your height is {height}, and did you win? {winning}" )