import random

########################
# List comprehension
print("\n\n# List comprehension")
names = ["Christian", "Kristen", "Budi"]
new_list = [name.upper() for name in names if len(name) > 5]
print(names)  # Output: ['Christian', 'Kristen', 'Budi']
print(new_list)  # Output: ['CHRISTIAN', 'KRISTEN']

num_list1 = [1, 2, 3, 4]
num_list2 = [1, 2, 3, 5]
overlap_list = [num for num in num_list1 if num in num_list2]
print(overlap_list)  # Output: [1, 2, 3]

########################
# Dictionary comprehension
print("\n\n# Dictionary comprehension")
students = ["Christian", "Kristen", "Budi"]
student_dict = {student: random.randint(1, 100) for student in students if len(student) > 5}
print(student_dict)  # Output: {'Christian': 3, 'Kristen': 93}

########################
# For loop
print("\n\n# For loop")
# for (int i = 1; i < 13; i += 2)
# Output: 1 3 5 7 9 11
for i in range(1, 13, +2):
    print(i)
