
########################
# List
print("\n\n# List")
names = ["Christian", "Kristen"]
for name in names:
    print(f"- {name}")

for index, name in enumerate(names):
    print(f"- {index} - {name}")

########################
# 2D list
print("\n\n# 2D list")
foods = [["spinach", "wortel", "lettuce"], ["apple", "orange", "grape", "mango"]]
for food_category in foods:
    for food_item in food_category:
        print(f" - {food_item}")

########################
# Generate list using range
print("\n\n# Generate list using range")
numbers = range(1, 11) # generate numbers from 1 to 10
for number in numbers:
    print(number)

########################
# For loop
print("\n\n# For loop")
for i in range(5):  # 0 to 4
    print(i)

for char in "hello":
    print(char)

########################
# While loop
print("\n\n# While loop")
i = 0
while i <= 10:
    print(f"i : {i}")
    i += 1
