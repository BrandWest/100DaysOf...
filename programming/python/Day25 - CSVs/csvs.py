'''
    Pandas

    
    Tabular data = CSVs (comma,separated,values)
'''
import csv
import pandas

if __name__ == "__main__":
    '''WITH NO IMPORTS'''
    # data = []
    # with open ("files/weather_data.csv", "r") as data_file:
    #     data = data_file.readlines().strip('\n')
    #     # data.append(line.strip('\n'))

    # print(data)

    ''' WITH CSV'''
    # temp = []
    # with open ("files/weather_data.csv", "r") as data_file:
    #     data = csv.reader(data_file)
    #     print(data)
    #     for row in data:
    #         if "temp" not in row:
    #             temp.append(int(row[1]))
    # print(temp)
    

    ''' WITH PANDAS'''
    data = pandas.read_csv("files/weather_data.csv")
    print(data)