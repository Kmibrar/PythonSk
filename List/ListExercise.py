# Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500] # output [500, 400, 300, 200, 100]
# list1.reverse()               # Solution 1

# for i in range(len(list1)):
#     list1.reverse()
#     print(list1[i])           # solution 2
# print(list1)

# list1=list1[::-1]
# print(list1)                  # Solution 3
# Completed
#---------------------------------------------
# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item
# from both the list, then the 1st index item, and so on till the last element.
# any leftover items will get added at the end of the new list.

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"] #Expected output:['My', 'name', 'is', 'Kelly']

# list3 = zip(list1,list2)
# list3 =[i+j for i,j in zip(list1,list2)] # type cast the item if not same
# print(list3)
# Completed
# ---------------------------------------------
# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# numbers = [1, 2, 3, 4, 5, 6, 7] # Expected output:[1, 4, 9, 16, 25, 36, 49]
# sqr =[]
# for i in numbers:
#     sqr.append(i*i)
# print(numbers)
# print(sqr)                # solution 1

# res = [i*i for i in numbers]
# print(numbers)
# print(res)                # solution 2

#--------------------------------------------------
# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"] # Expected output:['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list3 = [x+y for x,y in zip(list1,list2)]
# print(list3)              # solution
#--------------------------------------------------
# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100

# for x,y in zip(list1,list2[::-1]):
#     print(x,y)                        # solution
#-------------------------------------------------
# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # Expected output:["Mike", "Emma", "Kelly", "Brad"]
# list2=list(filter(None,list1))
# # print(list2) # completed
# -------------------------------------------------
# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # Expected output:[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# print(list1)
# l=list1[2][2]
# l.append(7000)
# print(list1)                  # solution
# Completed
#------------------------------------------
# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by
# adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# # sub list to add
# sub_list = ["h", "i", "j"]
# # Expected Output:['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# l=list1[2][1][2]
# l.extend(sub_list)
# print(list1)
#--------------------------------------------------------
# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item.

# list1 = [5, 10, 15, 20, 25, 50, 20]
# # Expected output:[5, 10, 15, 200, 25, 50, 20]
# index = list1.index(20)
# list1[index]=200
# # print(list1)                      # solution
#-------------------------------------------------
# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# # Expected output:[5, 15, 25, 50]
# while 20 in list1:
#     list1.remove(20)
# # print(list1)                      # 1 solution
# ------------------------------------------------
# Exercise 1: Write a program to create a list with random data types elements.
# Hint
# List should look like
# [22, ‘PythonLobby’, 22.3]

# num = [22,"python",3.4]
# print(num)
# # print items with it's type
# for i in range(len(num)):
#     # print(num[i],type(num[i]))        solution
#---------------------------------------------
# Exercise 2: Write a program to print all the elements of a list in single line.
# Hint
# num = [23,24,54,34]
# Expected output 23  24  54  34
# for i in num:
#     print(i, end=" ")                 # solution 1

# for i in range(len(num)):
#     print(num[i],end=" ")             # solution 2
# ------------------------------------------------
# Exercise 3: Write a program to count the number of items stored in a list.
# Hint
# num = [23, 34, "hello", 32, 56]
#
# # Expected output Total count of items are: 5
# count =0
# for i in range(len(num)):
#     count+=1
# print("Total count of items are :", count)    # solution
# print(" Total number of items are ",len(num))
#------------------------------------------------
# Exercise 4: Write a program to reverse a list in Python.
# Hint
# num = [23, 34, "hello", 32, 56]
# Expected output # [56, 32, ‘hello’, 34, 23]
# num.reverse()
# print(num)                            # solution
# print(num[::-1])                      # solution
# ------------------------------------------------
# Exercise 5: Python program to square each element of a list.
# Hint
# x = [2, 3, 4, 5, 6]
# # Expected output # Result : 4 9 16 25 36
# y = []
# for i in x:
#     y.append(i * i)
# print(y)

# res = [i*i for i in x]
# print(x)
# print(res)                #

# ----------------------------------------------------
# Exercise 6: Python program to remove an empty element from a list.
# Hint
# num3 = [7,"",40,"hello",34,45,""]
# # # Expected output Result : [‘Hello’, 34, 45, 40]
# num2 = list(filter(None,num3))
# print(num2)

# while ("" in num3):
#     num3.remove("")
# print(num3)

# ---------------------------------------------------------
# Exercise 7: Python program to append an element to a list.
# Hint
# num = [23,45,67,8,9]
# Enter the item to insert: study
# Expected output # Result: [23,45,67,8,9, ‘study’]
# num.append("study")
# print(num)
# ----------------------------------------------------------
# Exercise 8: Write a program to display those items from a list that is divisible by 5.
# Hint
# num = [3, 5, 7, 9, 23, 15]
# Expected output Result: 5  15
# for i in num:
#     if  i % 5 == 0:
#         print(i)
#
# a = [i for i in num if i % 5 == 0]
# print(a)
# -------------------------------------------------------------
# Exercise 8: Write a program to sum all the elements of a list.
# Hint
# num = [2,3,2,4,7,8]
# Expected output Sum of list items 26
# num2=sum(num)
# print(num2)
# -------------------------------------------------------------
# Exercise 9: Write a program to get the maximum number from a list.
# Hint
# num = [2,3,2,4,7,8]
# # Expected output # Max number in list items is 8
# num2 = max(num)
# print(num2)
# -------------------------------------------------------------
# Exercise 10: Write a program in Python to remove duplicate items from a list.
# Hint
# num = [2,3,4,5,2,6,3,2]
# # Expected output Result: [2, 3, 4, 5, 6]
# num2 = []
# for i in range(len(num)):
#     if num[i] not in num2:
#         num2.append(num[i])
#     else:
#         pass
# print(num2)
# ------------------------------------------------------------
# Exercise 11: Write a program in Python to choose a random item from a list.
# Hint
# import random
# num = [2,3,4,5,6,8,9]
# # Expected output Result: 6
# a=random.choice(num)
# print(a)
# ------------------------------------------------------------
# Exercise 12: Write a program to append data of the second list to the first list.
# # Hint
# list1 = [23, 24, 25, 26]
# list2 = [27, 28, 29, 30]
# # Expected output
# # Result: [23, 24, 25, 26, 27, 28, 29, 30]
# list3 = list1 + list2
# print(list3)
# -----------------------------------------------------------------
# Exercise 13: Write a program in Python to filter odd and even number from a list.
# # Hint
# given = [2, 23, 24, 51, 46, 67]
# # Expected output  Even [2, 24, 46] Odd [23, 51, 67]
# odd = []
# even = []
# for i in given:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(" list of Even Number : ",even)
# print(" list of Odd Number  : ",odd)
# --------------------------------------------------------------------
# Exercise 14: Write a program to enter or append n numbers in a list.
# Hint
# Input: 2
# Enter element at index 1: 2
# Enter element at index 2: 4
# Expected output  Result: [‘2’, ‘4’]
# a =[]
# b = int(input("How many elements you want to enter: "))
# count =1
# for i in range(b):
#     x= input(f"Enter element at index{count} : ")
#     count +=1
#     a.append(x)
# # print(a)
# ----------------------------------------------------------------------
# num = []
# n = int(input("How many elements you want to enter: "))
# count = 1
# for i in range(n):
#     x = input(f"Enter element at index {count}: ")
#     count += 1
#     num.append(x)
#
# # printing list after item insertion
# print(num)
# ------------------------------------------------------------------
# Exercise 15: Write a program in Python to remove repetitive items from a list.
# Hint
# num = [2,3,4,5,2,6,3,2]
# # Expected output  Result: [2, 3, 4, 5, 6]
# new_list=[]
# for i in num:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)
# -------------------------------------
# Tast by Aftab bhai

# a = [5,3,4,5,6,7,4,4,5,6,[7,8,65,4,3,3,5,67,8,9,0,76,5],4,
# b = [x*3 for x in a if x == 3]
# print(b)
# ------------------------------------------
# a = [5,3,4,5,6,7,4,4,5,6,[7,8,65,[4,3,[3,5,67],8,9],0,76,5],4]
# # for b in a:
# # print(a[10])
# b=a[10]
# print(b)
# c=[x*3 for x in b]
# print(c)
# print(c[-2])
# c[-2]="Sami"
# print(c)
#--------------------------------------------------------------------------------------
list1 = [5, 3, 4, 5, 6, 7, 4, 4, 5, 6, [7, 8, 65, [4, 3, [3, 5, 67], 8, 9], 0, 76, 5], 4]
# Value to find in list1
value_to_find = 67
# Using a for loop with conditionals
found = False
for item in list1:
    if isinstance(item, list):
        # If the item is a list, check its elements
        for nested_item in item:
            if str(value_to_find) in str(nested_item):
                print(f"Value {value_to_find} found in the nested list!")
                found = True
                break
    else:
        if item == value_to_find:
            print(f"Value {value_to_find} found in the list!")
            found = True
            break

if not found:
    print(f"Value {value_to_find} not found in the list.")










# for x in a:
#     if type(x) is list and len(x) == 7:
#         var = x[3][2]
#         print(var)




# b= [x for x in a if type(a) == list]
# if type(a) == list:
#     for x in a:
#         if x == list:



        # print(type(x))
        # print(x)

# print(list(x))
# print(b)

