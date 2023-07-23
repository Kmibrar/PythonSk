# Task: Word Count
# Write a program that counts the number of words in a given sentence.
# The program should ask the user to enter a sentence, and then it should
# calculate and display the total number of words in that sentence.


user_input = input("Enter a sentence: ")

user_input = user_input.replace(" ", "")  # Remove whitespace

length = len(user_input)
words = user_input.split()

print("Length of input (excluding whitespace):", length)
print("Words in input (excluding whitespace):", words)

# Completed
