
########################
# If statements
print("\n\n# If statements")
word = "word";
if word == "word":
    print("The value is word")
elif word == "not word":
    print("The value is not word")
else:
    print("The value is " + word)

########################
# Switch case using dictionary
print("\n\n# Switch case using dictionary")
def switch_case(option):
    switch_dict = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3"
    }
    return switch_dict.get(option, "Default case")  # Default case if not found

print(switch_case(2))
print(switch_case(4))
