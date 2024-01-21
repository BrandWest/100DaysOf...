'''
functions
	easy code blocks
    Complex instructions + packaging

functions with inputs 
	def function(variable)
		#do something with variable
        then this
        then do this.
	
        return variable
        
functions with positional arguments is the default
	def function( positionalArg1, positionalArg2):

    
functions with keyword arguements
	def function (a=1, c=2, b=3)
'''


def greet():
    print("one things")
    print("two things")
    print("three things")
    
greet()


def greetings(name):
    print(f"Hello {name}")
    
# name = input("Whats your name? ")
# greetings(name)

#poistional function
def greeting(name, location):
    print(f"Hello {name}, how is the weather in {location}")
    
name = input("Whats your name and location? ")
location = input ("whats your location? ") 
greeting(location = location, name = name)




