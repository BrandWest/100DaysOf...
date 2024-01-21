'''
    This is unique to python
    new list from a previous list.
    instead of for loops

    number = [1,2,3]
    new = []
    for n in numbers:
        add_1 = n+1
        new.append(add_1)
    
        

    new_list = [new_item for item in list ]

    name of the new list
    [] <- for the list
    new_item <-- this is the comprehension
    for <- for loop
    item <- the new
    in
    list <- the old list (or the one we're iterating through)


'''

numbers = [1,2,3]
new = []
for n in numbers:
    add_1 = n+1
    new.append(add_1)

#new_list = [new_item for item in list ]
new_list = [ n+1 for n in numbers]

print(numbers, new_list)

name = "Brandon"

letter_list = [ letter for letter in name ]
print(letter_list)
'''
    Python Sequences 
        A list
        range
        string
        tuple
    A sequence is a specific order
        These comprehensions are done in an order
        Takes each item in the order and do something to it.
'''

doubled = [ number * 2 for number in range(1,5)]
print(doubled)


'''
    Conditinoal list comprehension
    new_list = [new_item FOR item IN list IF test]
    will only add and perform the code, if the test passes or not
'''

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Create a list that only have 4 letters or less.
short_names = [ name for name in names if len(name) <= 4]
print(short_names)

upper_names = [ name.upper() for name in names if len(name) > 5]
print(upper_names)