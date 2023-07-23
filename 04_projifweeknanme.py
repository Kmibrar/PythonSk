# Task: Weekday Name Detector

# Problem statement:
# Write a Python program that takes a numeric input representing a day of 
# the week (1 for Monday, 2 for Tuesday, etc.) and outputs the corresponding 
# name of the weekday. If the user enters an invalid number (less than 1 or 
# greater than 7), the program should print an error message.

weekday = input("Please Enter a number between 1 to 7 : ")
if weekday == "1":
    print("it is Monday")
elif weekday == "2":
    print("it is Tuesday")
elif weekday == "3":
    print("it is Wednesday")
elif weekday == "4":
    print("it is Thursday")
elif weekday == "5":
    print("it is Friday")
elif weekday == "6":
    print("it is Saturday")
elif weekday == "7":
    print("it is Sunday")
else:
    print("ERROR: Your have input Invalid value Please Enter a number btw 1 to 7 ")

# Completed
