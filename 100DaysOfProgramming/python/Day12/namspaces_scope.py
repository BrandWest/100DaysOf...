'''
    Scope: a variable inside functions, vs global, vs local

    a function with local scope called outside will provide a NameError: name "variable" is not defined.

    A namespace is valid within certain scopes in general.
'''
#global scope
player_health = 10


#local scope
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
# print(potion_strength)


#Namespace
'''
    drink poition is in the namespace of game.
'''
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)


'''
Block scope
    within if statements and a new varialbe is in the if catch - it does not have block / local scope to that if statement

'''

game_level = 3
enemies = ["sekelton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

'''
    Modify a global scope variable
    #local scope example

#enemies is global.
enemies = "skeleton"

def increases_enemies():
    #enemies is local
    enemies = "zombie"
    print(f"enemeies inside function: {enemies}")

increases_enemies()
print(f"enemeies outside of function: {enemies}")
'''
'''#local scope example

#enemies is global.
# enemies = "skeleton"

def increases_enemies():
    global enemies #Not best practice to change global scope variables
    # enemies = "zombie"
    print(f"enemeies inside function: {enemies}")

increases_enemies()
print(f"enemeies outside of function: {enemies}")'''

'''
    Global Constants
        pi = 3.1415926
        This is a good constant
'''
PI = 3.1415926
URL = "https://www.google.ca"
TWITTER_HANDLE = "@twitter_handle"

def calc():
    print(PI)