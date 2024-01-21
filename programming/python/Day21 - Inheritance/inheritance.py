'''
    Used to make it easier to add/leverage some functinos etc.
    Pastry Chef will do some of what the chef knows.

    Class Inheritance 
        Chef
            bake()
            stir()
            measure()
        class Pastry_Chef(Chef):
            knead()
            whisk()

    Can in herit both features and methods.
'''
#this is how you do the inheritance.
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__() #This refers tot he super class (parent) initalize everything the usper class can do.


    def swim(self):
        print("Moving in water.")


    def breath(self):
        super().breath() #Calls the suepr classes method, then add to it.
        print("doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)