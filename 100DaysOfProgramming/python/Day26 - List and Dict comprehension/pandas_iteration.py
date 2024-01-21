''''


'''

student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56,76,98]
}

#looping through dictionaries
for (key, value) in student_dict.items():
    print(value)


import pandas

student_dataframe = pandas.DataFrame(student_dict)

print(student_dataframe)

#loop through the DF
# for key,value in student_dataframe.items():
#     print(key,value)

#Pandas loops (ITERROWS)
for (index, row) in student_dataframe.iterrows():
    # print(row.student) #These are all pandas series
    if row.student == "angela":
        print(row.score)