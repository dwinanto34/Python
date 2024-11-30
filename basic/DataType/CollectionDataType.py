
########################
# List
print("\n\n# List")
names = []
names.append("Christian")
names.append("Kristen")
names.remove("Christian")
print(names)
print("non-existent" in names)

# 2D list
print("\n\n# 2D List")
foods = [["spinach", "carrot", "lettuce"], ["apple", "orange", "grape", "mango"]]
print(foods)
print(len(foods)) # 2
print(len(foods[0])) # 3
print(len(foods[1])) # 4

########################
# Tuple (Immutable, we can't modify the element after creation, only concatenation operatios are allowed)
print("\n\n# Tuple")
tuple_data = ("string", 1, False)
tuple_data = tuple_data + (0.1, True)
# Single-element tuple (must include a trailing comma)
tuple_data = tuple_data + ("new string",)
print(tuple_data)
print(tuple_data[0])
print(tuple_data[1])
print(tuple_data[2])
print(tuple_data[3])

########################
# Dictionary (HashMap)
print("\n\n# Dictionary")
customer_map = {"name": "Christian", "age": 31}
for key in customer_map:
    print(f"{key} {customer_map[key]}")

food_map = {}
food_map["vegetables"] = ["spinach", "carrot"]
food_map["fruits"] = ["apple", "orange"]
food_map["invalid data"] = ["invalid data"]
if "invalid data" in food_map:
    del food_map["invalid data"]

for key, value in food_map.items():
    print(f"{key} : {value}")

########################
# HashSet
print("\n\n# HashSet")
name_set = set()
name_set.add("name_set 1")
name_set.add("name_set 1")
name_set.add("name_set 2")
name_set.add("name_set 3")
name_set.remove("name_set 3")
print(name_set)
print("non-existent" in name_set)

name_set2 = {"name_set2 1", "name_set2 1", "name_set2 2"}
print(name_set2)
