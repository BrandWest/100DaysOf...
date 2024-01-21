'''
    Files: 
        Read: 
        Write: Writing will let you append it.
    With: Manages the file directly and dont need a open/close function

    Relative paths: Relative to the folder you're currently in
    Absolute Paths: the complete path to the file you are accessing

    The relative path can be identified by ..(previous folder)
        ../ <- Previous directory
        ./ <- current directory

'''

with open (file="../files/files.txt", mode='r') as file:
    for line in file:
        print(line)

with open (file="../files/files.txt", mode='a') as file:
    file.write("\nThis is new text.")


with open (file="../files/files.txt", mode='r') as file:
    for line in file:
        print(line)