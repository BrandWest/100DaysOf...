'''
Procedual (functions) that do particular things.
        One prcoedure leads to another.
        Top to bottom 
        Earliest programming paradigm.

Object Orientied Programming
    Simple coding relationships
    self driving card
        camera
        lane detection
        navigation
        fuel management
        
    Reusability
        Going from self driving car to drone
    
    Splitting a larger task into smaller pieces.
    Imagine running a resturant
        Receptionist
            Reserveing seats for visitors
        Waitress
            Brining the order
        chef
            create the thing they ordered
        cleaner
            tidying up after
        
    Each person has their own role
        Water knows how to wait
        Chef knows how to cool
        manager will manage all staff to manage what to do
        

How to use OOP
    Classes using resturant exmaple
        staff
            waiter
            chef
            cleaner
        manager
            controls staff
    Models 
    modle of a waiter
        What it Has: Attributes
            Is it holding a plate?
                is_holding_plate = True
            What tables are they responsible for
                tables_responsible = [4,5,6]
        
        What it does: METHODS
            Takes an order to the chef
                def take_order(table, order):
                    #takes order to chef
            take payments
                def take_playment(amount):
                    #add money
    OOP trying to modle real life objects that have attributes that they have (variables) and methods that they do (methods modled by functions)
    an object combines data and functinoality.

    You can have multiple objects from same type
        Can make mulitple versions of the same object
            Henry waiter
            Betty waitress
    in oop - blueprint a class.
    each object in the class is called an object.

Classes
    Class Car
        color
        wheels
        milage
        fuel
    Object
        drive
        stop/break
'''

'''
    Classes are PascalCase (title case)
        #object is the car
        #car blueprint is the class

    car = CarBlueprint()
'''
#Turtle Graphics

