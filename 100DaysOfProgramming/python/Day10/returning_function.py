'''
How functions really work and how to use them to reduce redundant code.

Functions
    def function(a,b,c):
        do x
        do y
    
        return x,y


    result = function(a,b,c)
'''


#functions with outputs title cases
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Strings can not be empty."
    return first_name.title() + " " + last_name.title()

print(format_name (input("Please insert first name string: "), input ("Please input last name string: ")))


#More than one return statements