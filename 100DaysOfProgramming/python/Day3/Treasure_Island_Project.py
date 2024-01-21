print('''
*******************************************************************************
		  |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
		  |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
		  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("You are at a crossroads, do you want to go left or right? Type: \"Left\" or \"Right\" ")
if direction.lower() != "left":
	print("You walk and fall in a hole. Game Over.")
	exit()

direction = input("You come to a lake, do you want to wait or swim across? Type: \"Wait\" or \"Swim\" ")
if direction.lower() != "wait":
	print("You start swimming in the water, and are attacked by a trout. Game Over.")
	exit()
direction = input("The boat arrives and you are taken to the island. You come to a set of three doors, which do you choose? Type: \"Red\", \"Blue\", \"Yellow\" ")
if direction.lower() != "yellow":
	if direction.lower() == "red":
		print("You enter the red door and walk in, after some time you realize you are lost. A fire starts to spread. Game Over.")
		exit()
	else:
		print("You enter the blue door. You begin walking and realize there are no lights within the walkway, you continue to walk. You trip and fall into a hole. Game Over.")
		exit()
else:
	print("You enter the yellow door, you come to another door, open it. You found the treasure! YOU WIN!")
	exit()