fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(f"fruit pie")
    else:
        print(fruit + " pie")

make_pie(int(input("Enter a number: ")))
