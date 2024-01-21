'''
a dictionary
	work like a dictionary in real life
		Code: program instructionsfor the computer
        
    They allow us to group and tag related inforamtion
    Think a table
		Key : Value
        Bug : an error in a program that rpevents the program running as expected

	{Key: Value}

'''
#this is best practice
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
	"Loop": "The action doing something repeatedly",
}

print(programming_dictionary)

'''
To access the dictionary elements by fetching the key from dictionary

'''

print(programming_dictionary["Bug"])

'''
Errors
	KeyError: the key doesnt exist
	print(programming_dictionary["Bog"])

	Wrong data types
	keys that are not strings

    
To add an item to the dictionary    
'''
programming_dictionary["Loop"] = "The run constantly"

print(programming_dictionary)

'''
Creating empty dictionary
	empty_dic = {}
'''

#wipe an exisiting dict
# programming_dictionary = {}
print(programming_dictionary)

#Loop through a dict
for key in programming_dictionary:
    print(programming_dictionary[key])


