# Import the random module here
import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "Brandon,Debbie,Callum"
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
paying = names[random.randint(0, len(names))]
print(f"{paying} is going to buy the meal today!")