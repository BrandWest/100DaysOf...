import pandas as pd


''' I need
    Squirrl Colors (Primary Fur Color)
    count
'''
def get_file():
    filepath = "/home/caboose/codingProjects/python/udemy/Day25 - CSVs/files/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    return pd.read_csv(filepath)
    
def get_colors_count(data):
    gray = 0
    red = 0
    black = 0

    for color in data.PrimaryFurColor:
        if color == "Gray":
            gray += 1
        elif color ==  "Cinnamon":
            red += 1
        elif color ==  "Black":
            black += 1

    return gray, red, black

def get_colors(data):
    
    colors = data.PrimaryFurColor.unique()
    gray, cinnamon, black = get_colors_count(data)

    color_dict = {
        "Fur Color" : ["grey", "red", "black"],
        "Count" : [gray, cinnamon, black]
    }

    return color_dict

if __name__ == "__main__":
    squirrel_data = get_file()
    colors = get_colors(squirrel_data)
    colors_dataframe = pd.DataFrame(colors)
    colors_dataframe.to_csv("files/squirrl_colors.csv")