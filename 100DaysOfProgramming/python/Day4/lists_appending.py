'''
Lists are data structures, organization and storage.

Data that is connected to one another.

order in the data - All people in a queue (queue order)


Lists
				0		1	  2
	fruits = [item1, item2, item3]
'''

# fruits = ["banana", "apple", "cherry"]

#names of the states of the US.

states = ["New York", "Delaware", "Pennsylavania" ]

#To access the list is the index/offset of the item that we want.
print(states[1])

print(states[-1]) #This will give you the list from the end

#to change the list item 
states[2] = "PV"
print(states)

states.append("old york")

print(states)
#docs.python.org/3/tutorial/datastructres.html for new lists
state = ["Brandonland", "Debbieland"]
states.extend(state)
print(states)