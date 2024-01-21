'''
    Higher order functions
        These functions (like the calculator example)
        will take a function along with these others, in order to do some work based on the function itself.
        so the calculator takes 2 numbers and a function called func
        when run with calculator(2,3,add) you will get 5.
        When doing htis, you do NOT add () otherwise you will fire that functino right away.

def add(n1, n2):
    return n1 + n2

def subract(n1, n2):
    return n2 - n1

#Taskes ANY functions as an input and this funct will trigger.
def calculator(n1, n2, func):
    return func(n1, n2)

    Event listeners
        Looking for user input (key input)
        
'''


from turtle import Turtle, Screen

'''
    This function is used as an input
    when passed into a listener it fires only then.
'''
def move_forwards():
    tim.forward(10)
    

if __name__ == '__main__':
    #objects
    tim = Turtle()
    screen = Screen()

    #must define a function for a listening.
    screen.listen()
    #We dont add parentheses in the onkey method and will trigger after the key is pressed.
    #when using predeffined functions like onkey - use keywords not positional.
    screen.onkey(key="space", fun=move_forwards)
    screen.exitonclick()