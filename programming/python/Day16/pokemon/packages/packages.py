'''
    importing and getting packages
    each file in the project is a module in itself.
    a package is a number of modules.

    Creating a table of pokemon and type
'''

from prettytable import PrettyTable
pokemons = {
    1 : {
        'name' : 'Squritle',
        'type' : 'Water',
    },
    2 : {
     'name' : 'Charmander',
     'type' : 'Fire',
    },
    3 : {
        'name' : 'Pikachu',
        'type' : 'Electric',
    },
}
table = PrettyTable()

#Field names (titles) of the columns
table.field_names = ['Pokemon Name', 'Pokemon Type']

#This will change the variable attributes
table.align = 'l'

for index in range(len(pokemons)):
    table.add_row([pokemons[index+1]['name'],pokemons[index+1]['type']])
print(table)


# table.add_column("Pokemon Name, []")