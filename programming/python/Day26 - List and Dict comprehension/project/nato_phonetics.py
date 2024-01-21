import pandas

def get_name():
    return input("Enter a word: ")
    

def get_nato_spelling(name, data):
    name_list = [ letter.upper() for letter in name ]
    phonetic_name = [ row.code for letter in name_list for (index,row) in data.iterrows() if letter == row.letter]
    print(phonetic_name)


def get_file():
    return pandas.read_csv("project/data/nato_phonetic_alphabet.csv")


if __name__ == "__main__":
    dataframe = get_file()
    name = get_name()
    get_nato_spelling(name, dataframe)