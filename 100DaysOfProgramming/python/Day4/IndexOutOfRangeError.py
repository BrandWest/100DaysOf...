'''

'''

states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island",
                     "Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin",
                     "California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma",
                     "New Mexico","Arizona","Alaska","Hawaii"]

num_of_states = len(states_of_america)
print(states_of_america)

print(len(states_of_america))

# print(states_of_america[50]) #Index error list index out of range or OFF BY ONE
# print(states_of_america[num_of_states]) #Index error list index out of range or OFF BY ONE
print(states_of_america[num_of_states - 1]) 


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "potatoes"]

fruits = ["Strawberries"]
vegtables = ["Spinach"]
dirty_dozen_nested = [fruits, vegtables]

print(dirty_dozen_nested)