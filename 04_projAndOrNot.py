# Task: Logical Operators Practice - Eligibility Checker with Multiple Conditions

# Problem statement:
# Write a Python program to check a person's eligibility for driving a car in a country. The program should take input for the person's age and nationality and then determine whether they are eligible to drive or not. The eligibility criteria are as follows:

# A person must be at least 18 years old to be eligible to drive.
# Only citizens of the country are eligible to drive.
# Additionally, if the person is 16 or 17 years old, they can drive if they have a valid learner's permit.
# Instructions:

# Prompt the user to enter their age and nationality.
# Use logical operators (and, or, not) to check whether the person meets the eligibility criteria.
# Print out a message indicating whether the person is eligible to drive or not.

age = int(input(" Enter your age : "))
nationality = input("Are you the citizen of the country (yes/no) ")

# print("yes" in nationality)
# print("no" in nationality)
if age >= 18 and age <= 60 and nationality == "yes" or nationality == "YES":
     print(" you are " + str(age) + " old ")
# elif nationality == "yes" or nationality == "YES":
     print("You are the citizen of this country ")
# elif nationality == "no" or nationality == "NO":
    
else: print(" Please Enter yes/no Only")
print("Sorry you are not the citizen of this country ")

