# Task: Student Grading System

# Problem statement:
# Write a Python program that takes input for a student's score (out of 100) and 
# assigns a letter grade based on the score. The grading criteria is as follows:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# Instructions:
 
# Prompt the user to enter the student's score.
# Use if, elif, and else statements to determine the letter grade based on the score.
# Print out the calculated letter grade.

Marks = int(input(" Please Enter your Marks (out of 100 ):  "))

if 90 <= Marks <= 100:
    print(" you have got : A Grade ")
elif 80 <= Marks < 90:
    print(" You have got : B Grade ")
elif 70 <= Marks < 80:
    print(" You have got : C Grade ")
elif 60 <= Marks < 70:
    print(" You have got : D Grade ")
elif 0 <= Marks < 60:
    print(" You have got : E Grade ")
else:
    print("please Enter Marks out of 100 ")

# completed
