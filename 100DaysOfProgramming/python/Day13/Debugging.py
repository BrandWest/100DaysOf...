'''
    Debugging:
        1. Describe the problem we're having and make sense of whats going on.
        2. Reproduce the issue
        3. Play Computer
        4. Editor helping
        5. Print statements
        6. Debugger
        7. Take a break and step away
        8. Ask a friend
        9. Run the code often and do each one at a time
        10. Ask StackOverflow
'''

############DEBUGGING#####################

# Describe Problem
'''
    The for loop is indexing i between a range of 1 to 20 (19)
    You got it does not print because i never reaches 20.

    Fixed function below
'''
# def my_function():
#   for i in range(1, 20):
#     #It never reaches here because it never goes to 20
#     if i == 20:
#       print("You got it")
# my_function()

# def my_function_fixed():
#   for i in range(1, 21):
#     #It never reaches here because it never goes to 20
#     if i == 20:
#       print("You got it")
# my_function_fixed()

# # Reproduce the Bug
'''
    the code is printing out the numbers of dice faces from a list
    a list starts at 0 and ends at 5 (= 6 elements.) Because of this
    The list is going out of range because its attempting to access the 
    6th item dice_imgs[6] which doesnt exist. Another issue is that 1 does not get chosen

    modified code to run on a loop. found it crashes on 6 as expected.
'''
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]

# while True:
#     dice_num = randint(1, 6)
#     print(dice_num)
#     print(dice_imgs[dice_num])
# print(dice_imgs[dice_num])
'''
    Fixed code
'''
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num-1])

# # Play Computer
'''
    The code should check if a year falls between 1980 and 1994
    if this is the case they are a mellenia.
    otherwise theya re larger than 1994 youre a gen z

    problem: The year will never evaluate 1994 as there is no =>
'''
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

'''
    Fixed code
'''
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
'''
    no indent for if statemnt

    a second bug, the age is a string and not an int.

    a third error no f string 
'''
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

'''
    Fixed code
'''
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
'''
    The calculation to get the number of words per page.
    The bug: equality not equals
'''
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

'''
    Fixed code
'''
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
'''
    the list given is supposed to multiple each list item by 2.

    bug, the list append is outside of the for loop, so its only getting 13*2
'''
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
'''
    Fixed COde
'''
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])