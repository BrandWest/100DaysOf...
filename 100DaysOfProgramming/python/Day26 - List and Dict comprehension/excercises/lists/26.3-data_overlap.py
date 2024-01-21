
with open ('file1.txt', 'r') as file1:
    file1_numbers = [ int(number.strip('\n')) for number in file1 ]

with open ('file2.txt', 'r') as file2:
    file2_numbers = [ int(number.strip('\n')) for number in file2 ]

result = [ number for number in file2_numbers if number in file1_numbers]

# Write your code above 👆
print(result)
