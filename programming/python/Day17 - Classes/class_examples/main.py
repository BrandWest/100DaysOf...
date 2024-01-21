'''
    #Class keyword Name of the class:
    #The name should be in 'PascalCaseNotation


    Constructors
        Specifies when the object is being constructed (inializing)
'''
class User:
    #What the have
    '''
        This is a special initalizing function used to initalize the attributes.
    '''
    def __init__(self, id, username):
        print("New user being created...")
        '''
            Provides the attributes into the init function which is added to the class 
            Somteimtes you dont want to have specific attributes with sepcific values. To not inilizies each of the objects
        '''
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    #what they can do
    '''
        Requires a self parameter so that it knows the object that  calls it.
        self is when dealing with classes.
    '''
    def follow(self, user):
        self.following += 1
        user.followers += 1
    

#initalizing the class through constructors
user_1 = User('001', 'brandon')
user_2 = User('002', 'deb')
print(user_1.id)
print(user_2.username)
print(user_1.followers)

user_1.follow(user_2)
print(user_1.following, user_1.followers)
print(user_2.following, user_2.followers)

'''
    #We can add attributes without defining it in the object

    Somteimtes you dont want to have specific attributes with sepcific values.
'''

# user_1.id = "001"
# user_1.username = "brandon"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "deb"

