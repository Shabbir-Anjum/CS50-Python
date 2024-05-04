def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip("_")
# Prompt the user for input
user_input = input("camelCase: ")

# Convert the input from camel case to snake case
snake_case_output = camel_to_snake(user_input)

# Output the result
print("Snake_case:", snake_case_output)
