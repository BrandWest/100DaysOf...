'''
try
except
else
finally

raise
    Raise our own exceptions
'''

# try:
#     with open ("a_file.txt", "r") as file:
#         file.read()
#     a_dict = { "key": "value"}
#     # value = a_dict["non_key"]
# except FileNotFoundError as e:
#     print(e)
#     #creates the file
#     open("a_file.txt", "w")
# except KeyError as e:
#     print(f"The key {e} does not exists")
# else:
#     content = open("a_file.txt", "r")
#     print(content.read())
# finally:
#     #Will run no matter what.
#     content.close()
#     raise TypeError("This is a type error I made")


'''Own Exception example'''
height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2

print(bmi)

if height > 3:
    raise ValueError("The height was too high.")