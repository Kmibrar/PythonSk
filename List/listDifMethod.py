# Create a list
# fruits = ["apple", "banana", "orange", "zaaa"]

# # append and extend
# fruits.append("grape") # append add ONLY ONE item at end of the list
# fruits.extend(["watermelon", "mango","red APPLE"]) # ADD many items as you want at the End
# insert
# fruits.insert(2, "pear") # insert add item ON THE Specific index(require 2 argument INDEX,ITEM)
#
# # remove
# fruits.remove("banana") # REMOVE Specific item (require an argument)
#
# # pop
# popped_fruit = fruits.pop(0) # POP Remove the last item by default and optional you can argument it index
# print((popped_fruit))

# # index and count
# print(fruits.index("orange")) # display the index of the item
# print(fruits.count("apple")) # display the quantity of the items
#
# # sorting
num = [2,4,763,2,1]
# num.sort() the items item should be of same only numeric or alphabet
# print(num) # sort (alphanumeric order)
# fruits.sort() # sort (alphabetical order) the items

#
# # reverse
# print(fruits.reverse()) # it reverse the order of alphabetic/numuaric
# print(num.reverse())


# # copy
# fruits_copy = fruits.copy() # create a copy of list
#
# print(fruits)
# print(popped_fruit)
# print(fruits_copy)

# print(fruits)







# fruits = ["apple", "banana", "orange", "mango", "apple"]

# Find the index of the first occurrence of "apple" in the list
# index_1 = fruits.index("apple")
# print("Index of 'apple':", index_1)
#
# # Find the index of "apple" starting the search from index 2
# index_2 = fruits.index("apple", 2)
# print("Index of 'apple' starting from index 2:", index_2)

# Find the index of "apple" between indices 1 and 4 (exclusive)
# index_3 = fruits.index("apple", 1, 5)
# print("Index of 'apple' between indices 1 and 4 (exclusive):", index_3)





# std = ["sami","noor","shafi","shafi" ,"inam","asmat"]
# print(std[4])# show the item on mention index number
# print(std[-1]) # show the item on mention index number


# Range of Indexes
# print(std[2:5]) # start form 2 and end at 5(-1)
# print(std[:5]) # form the start to 5(excluding)
# print(std[2:]) # from 2 to end
# print(std[-5:-3]) from -5 to -2

# check if item exists
# if "noor" in std:
#     print("yes 'noor' is available")