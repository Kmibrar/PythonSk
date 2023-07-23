# filter() function in Python
# In Python, the filter() function is used to return the filtered value.
# We use this function to filter values based on some conditions.
#
# Syntax of filter() function:
# filter(funtion, sequence)
# where,
# function – Function argument is responsible for performing condition checking.
# sequence – Sequence argument can be anything like list, tuple, string
# Example: lambda function with  filter()

l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_no = list(filter(lambda x: x > 0, l)) # Positive no only
print("Positive numbers are: ", positive_no)

negative_no = list(filter(lambda x: x < 0, l )) # Negative no only
print("Negative numbers are ",negative_no)