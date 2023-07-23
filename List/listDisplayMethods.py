# Getting Started With Python’s list Data Type
# Python’s list is a flexible, versatile, powerful, and popular built-in data type.
# It allows you to create variable-length and mutable sequences of objects.
# In a list,you can store objects of any type. You can also mix objects of different types within
# the same list, although list elements often share the same type

# Basic syntax
# days = ["monday", "tuesday", "wednesday", "thursday", "Friday", "saturday", "sunday"]

# To Display items we use the following method

# print(days)
# print(days[2])
# print(fruits.index("friday"))

# with for loop display the items only(loop through a list)
# for x in days:
# print(x)

# Loop Through the Index Numbers(for loop and range)
# for x in range(len(days)): # len() for int, as range only received int
#     print(x)

# Loop Through the Index Numbers(while loop)
# a = 0
# while a < len(days):
#     print(days[a])
#     a = a + 1

#     Looping Using List Comprehension
# [print(x) for x in days]

# Create a program which append the value of item starts with "s" in new list
# >>>>>>>>>>>>>>>>>>>>>>1.program
# new_list=[]
# for x in days:
#     if "s" in x:
#         if x[0]=="s":
#             new_list.append(x)
# print(new_list)

# >>>>>>>>>>>>>>>>>>>>>>2 program
# new_list=[]
# for x in days:
#     if x.startswith("s"):
#         new_list.append((x))
# print(new_list)


#  join() # it joint display all  the item(iterable objects & only string) all togather
# result = " ".join(days)
# print(result)

# # print("/".join(days))

# unpacking method to display item
# print(*days)

# display index and item in for loop by method (enumerate(list)
# for x in enumerate(days):
#     print(x)




