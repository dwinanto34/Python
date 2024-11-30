
########################
# Method
print("\n\n# Method")
def print_hi():
    print("hi")

print_hi()

########################
# Method Parameter
print("\n\n# Method Parameter")
def print_hi_with_param(name):
    print(f"hi, {name}")

print_hi_with_param("Christian")

########################
# Method Parameter with default value
print("\n\n# Method Parameter with default value")
def print_hi_with_param(name = "Default value is Kristen"):
    print(f"hi, {name}")

print_hi_with_param()

########################
# Method Parameter with argument list
print("\n\n# Method Parameter with argument list")
def sum_with_argument_list(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(f"sum, {sum}")

sum_with_argument_list(1, 2, 3)

########################
# Method with return value
print("\n\n# Method with return value")
def return_values():
    return "string", 1

stringVal, intVal = return_values()
tupleVal = return_values()
print(stringVal)
print(intVal)
print(tupleVal[0])
print(tupleVal[1])
