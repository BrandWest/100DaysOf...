'''
Nesting in Dictionaries
	Think of it as a folder
    a folder in a folder
    
    {
		key: value,
        key: [List],
		key: {Dictionary},
	}
'''

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dict
travel_log = {
    "France": ["Paris", "Lille", "Dikon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a dict in a dict
travel_log = {
    "France":{ "cities_visited": ["Paris", "Lille", "Dikon"],  "total_visits": 12 },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log)

'''
Nesting a dictionary in a List and good prgramming 
'''
travel_log = [
    { 
    	"country": "France",
        "cities_visited": ["Paris", "Lille", "Dikon"],
        "total_visits": 12 
	},
    { 
    	"country": "Germany", 
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]

print(travel_log)