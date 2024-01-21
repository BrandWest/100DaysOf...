'''
    DataFrame is a whole table file. (column and rows)
    Series are just the single column of data you may want.


    API Reference
        This is everything you can do with Pandas

        Serialization IO Conversion
            Can convert the data frome into different file types (html, dictionary, etc.)
'''


import pandas

data = pandas.read_csv("files/weather_data.csv")
'''DATA FRAME EXAMPLE'''
# print(data)
# print(type(data))
'''SERIES EXAMPLE'''
# print(data["temp"])
# print(type(data["temp"]))

''' Convert from dataframe to dic'''
data_dic = data.to_dict()
# print(data_dic)


'''Series convert to list'''
data_list = data["temp"].to_list()
# print(data_list)


'''Manual work'''
''' How to work out average temp'''
average = 0
for temp in data_list:
    average += temp

average = average / len(data_list)
# print(average)

'''Computation and Stats in pandas lib example'''
# print(data["temp"].mean())

# print(data["temp"].max())


'''Get data in columns'''
# print(data["condition"])
#This is much easier as its a class value
# print(data.condition)

'''get data in rows in dataframe'''
# print(data.day)
# print(data[data.day == "Monday"])

'''get data from max'''
'''
    Explination of this below
    data is or dataframe we are accessing
    data.temp is the series we're looking into
    data.temp.max() is the max value within that row.

    So the data DF is returning the value provided where the temp is the max. This is esentially filtering
'''
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print((monday.temp * 9/5) + 32)


'''Creating a dataframe'''
data_dict = {
    "students" : ['amy', 'angela', 'james'],
    "scores" : [76,65,56]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("files/new_data.csv")