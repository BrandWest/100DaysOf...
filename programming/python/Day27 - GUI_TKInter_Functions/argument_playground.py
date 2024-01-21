# To make this function more flexible.
def add(n1, n2):
    return n1+n2

'''
    You need * to accept any number of arguments. args is just a variable name.
    Args is a tuple (not changealbe.)
    You can access the args through the index too
    This allows us to specify an unspecified number of inputs
'''
def add(*args):
    temp = 0
    for n in args:
        temp += n
    return temp

print(add(1,2,3,4,5,6,7,8,9))


'''
    **KWARGS Many Keyworded Args
    unlimited keyword arguments

    kwargs is a dictinoary representing the keyword aguments key + values

    You can look through the inputs to find what you want, and to do something.
'''
'''
def calculate(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    
    print(kwargs["add"])
    print(kwargs["multiply"])
'''

# calculate(add=3, multiply=5)

'''
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
'''
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Mercedes-Benz", model="EQS")
print(my_car.model)

'''
    If something is not there, using .get() will return None
'''
my_car = Car(make="Mercedes-Benz")
print(my_car.model)


'''
    More "pythonic" stuff will have more standard default things
'''
