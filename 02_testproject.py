# Task: Simple Calculator

# Write a program that acts as a simple calculator. The program should ask the user to enter two numbers and an operator (+, -, *, or /). Based on the operator entered, the program should perform the corresponding arithmetic operation and display the result.

# Here are the steps to follow:

# Ask the user to enter the first number.
# Ask the user to enter the second number.
# Ask the user to enter an operator (+, -, *, or /).
# Use conditional statements (if, elif, else) to determine the operator and perform the corresponding operation.
# Display the result to the user.
# Example Output:

# mathematica
# Copy code
# Enter the first number: 5
# Enter the second number: 3
# Enter an operator (+, -, *, /): *
# Result: 15
# mathematica
# Copy code
# Enter the first number: 10
# Enter the second number: 2
# Enter an operator (+, -, *, /): /
# Result: 5.0
# This task will help you practice user input, conditional statements, and basic arithmetic operations in Python. Give it a try and see how you do!

x = float(input(" Enter your first Number: "))
y = float(input(" Enter your Second Number: "))
operator = input(" Enter operator:+, - , *, / ==> ")

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y
else:
    print("invalid operator")
    exit()

print("Result ", result)


# completed





z = x + y

print(z)










