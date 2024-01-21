'''
Randomization:
	Rolling Dice, etc.
    
    psudorandomness is how computers do the random functionality. Mersenne Twister is the python generators
    
	askpython.com
    
Modules
	are used to split the code up into individual modules. Each module are done via different code snippets.
    

'''

import random
from modules import my_module #This is my created module.

random_int = random.randint(1,10)
random_float = random.random()
random_uniform_float = random.uniform(1,5)

print(random_int, random_float, random_uniform_float)
print(random_float * random_int)
print(my_module.pi) #This pulls out the pi value from my_module

love_score = random.randint(1,100) 
print(f"Your love score is {love_score}!") #Based on the love calculator

