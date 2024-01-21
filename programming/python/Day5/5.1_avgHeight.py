
student_heights = input("Input a list of students heights ")
total_students = 0
total_height = 0
heights = student_heights.split(" ")

for height in heights:
    total_students += 1
    total_height += int(height)

print(round(total_height / total_students))