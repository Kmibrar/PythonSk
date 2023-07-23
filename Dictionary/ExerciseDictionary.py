# Exercise 1: Write a program to check whether a given key exists in a dictionary or not.
# Hint
# dict = {"0":1, "1":2, "2":3}
# # Input:
# # Enter value to check: 2
# # Expected output  Result: True
# num = int(input("Enter value to check :"))
# if num in dict:
#     print(True)
# else:
#     print(False)
# ----------------------------------------------------
# Exercise 2: Write a program to iterate over dictionary items using for loop.
# Hint
# dict = {0:"Value 1", 1:"Value 2"}
# # Expected output
# # Value of key 0 is Value 1
# # Value of key 1 is Value 2
# for key,val in dict.items():
#     print(f"Value of {key} 0 is :{val}")
# --------------------------------------------------------
# Exercise 3: Write a program to print only keys of a dictionary.
# dict = {0:"Value 1", 1:"Value 2", 2:"Value 3"}
# # Expected output , Result: dict_keys([0, 1, 2])
# keys = dict.keys()
# print(keys)
# ------------------------------------------------------------
# Exercise 4: Write a program to print values of dictionary.
# Hint
# dict = {0:"Value 1", 1:"Value 2", 2:"Value 3"}
# # Expected output dict_values([‘Value 1’, ‘Value 2’, ‘Value 3’])
# values = dict.values()
# print(values)
# --------------------------------------------------------------
# Exercise 5: Write a program in python to map 2 lists into a dictionary.
# # Hint
# keys = [1,2,3]
# values = ["Value 1", "Value 2", "Value 3"]
# # Expected output  {1: ‘Value 1’, 2: ‘Value 2’, 3: ‘Value 3’}
# dict = dict(zip(keys,values))
# print(dict)
# -------------------------------------------------------------------
# Exercise 6: Python program to remove a set of keys.
# Note: If we remove the key of the dictionary then the respective values of the dictionary should also be deleted. This means there are no values that exist without keys.
#
# # Hint
# my_dict= {0:"Value 1", 1:"Value 2", 2:"Value 3"}
# keys_to_remove = [0,1]
# # Expected output Result : {2: ‘Value 3’}
#
# for key in keys_to_remove:
#     del my_dict[key]
# print((my_dict))
# -----------------------------------------------------------
# Exercise 7: Python program to sort dictionary by values (Ascending/ Descending).
# d = {"key 1": 2, "key 2": 3, "key 3": 4}
# # Expected output
# # Ascending: [(‘key 1’, 2), (‘key 2’, 3), (‘key 3’, 4)]
# # Descending: [(‘key 3’, 4), (‘key 2’, 3), (‘key 1’, 2)]





# ---------------------------------------------------------
# Exercise 8: Write a program to concatenate two dictionaries to create one.
# dict1 = {"key 1": 2, "key 2": 3}
# dict2 = {"key 3": 4, "key 4": 5}
# # Expected output {‘key 1’: 2, ‘key 2’: 3, ‘key 3’: 4, ‘key 4’: 5}
# dict1.update(dict2)
# print(dict1)
# -------------------------------------------------------------
# Exercise 9: Write a program to sum all the values of a dictionary.
# dict1 = {"key 1": 200, "key 2": 300}
# # Expected output  Result: 500
# a=sum(dict1.values())
# print(a)
# ------------------------------------------------------------------
# Exercise 10: Write a program to get the maximum and minimum value of dictionary.
# dict1 = {"key 1": 200, "key 2": 300}
# Expected output
# Max: 300
# Min: 200
# val= dict1.values()
# max=max(val)
# min=min(val)
# print("max :",max)
# print("min :",min)
# --------------------------------------------------------------------
# Exercise 11: Write a program to check if a dictionary is empty or not.
# dict1 = {}
# # Expected output  Is dictionary empty ? : True
# if dict1 == {}:
#     print(True)
# else:
#     print(False)
# print(dict1)
# --------------------------------------------------------------------
# Exercise 12: Write a program in Python to choose a random item from a list.
# dict1 = {"key 1": 22, "key 2": 301}
# # # we are checking for 22 value
# # Expected output  Value exists in dictionary
#
# random_no = int(input("Enter the value :"))
# print(f" we are checking for {random_no}")
# val = dict1.values()
# if random_no in val:
#     print("Congragulation...! value exist in the list ")
# else:
#     print(" value does not exist ")
# ---------------------------------------------------------------------------
# Exercise 13: Write a program to sort dictionary values in python.
# dict1 = {
# "key 1": "Apple", "key 2":"Mango",
# "key 3":"Papaya"
# }
# Expected output
# key 1: Apple
# key 2: Mango
# key 3: Papaya
# for key in dict1.items():
# for key in sorted(dict1):
    # print(key,value)
    # print(f"{key} : {value}")
# ---------------------------------------------------------------------------
# # Exercise 14: Write a program to check whether a key exists in the dictionary or not.
# dict1 = {"key 1": 22, "key 2": 301}
# # Expected output # Key exists in dictionary
#
# if "key 2" in dict1:
#     print("key exist ")
# else:
#     print("no exist")
# --------------------------------------------------------------------------
# Exercise 16: Write a program in Python to remove repetitive items from a list.
# num = [2,3,4,5,2,6,3,2]
# # Expected output  Result: [2, 3, 4, 5, 6]
# num1 = []
# for val in num:
#     if val not in num1:
#         num1.append(val)
# print(num1)
# -------------------------------------------------------------------------
# Task: Word Frequency Counter with User Input
# Write a Python program that takes a paragraph or a multiline text
# as input from the user and counts the frequency of each word in the text.
# Display the word frequency in a dictionary format.
# res = {}
# parag = input("Enter a the text here :").lower()
# txt= parag.split()
# for a in txt:
#     if a not in res:
#         res.get(range,a)
# print(res)
#
# person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}
#
# # set default value if key doesn't exists
# person_details.setdefault('state')
# print(person_details)
# ---------------------------------------------------------------------------------
# a = ["a","t","r",{"no1": 5, "no2":10, "no3": 4 },"h","r"]
# b =[]
# # for i in a:
# #     if type(i) is dict:
# #         b.append(i)
# #     if b:
# #         b[0]["no1"] = 500
# # print(b)
# # l = [i for i in a if type(i) is dict and b.append(i)]
# # print(b.append(l))
#
# # print(b)
# person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}
# person_details.setdefault('state',)
# # print(person_details)
#
# person = {"name": "Jessa", "country": "USA"}
# # person['Country'] = 'Ap'
# # print(person['Country'])
# person.update({'countryes':'AA'})
# # print(person)
#
# person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
# # person.popitem()
# # print(person)
# deleted_item = person.pop('telephone')
# # print(deleted_item)  # output 1178
# # print(person)

# delete key 'weight'
# del person['weight']
# # display updated dictionary
# print(person)

# remove all item (key-values) from dict
# person.clear()
# # display updated dictionary
# print(person)  # {}
# person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}
#
# # Get the list of keys and check if 'country' key is present
# key_name = 'country'
# if key_name in person.keys():
#     print("country name is", person[key_name])
# else:
#     print("Key not found")
# dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
# dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}
#
# # copy second dictionary into first dictionary
# dict1.update(dict2)
# # printing the updated dictionary
# print(dict1)
#
# student_dict1 = {'Aadya': 1, 'Arul': 2, }
# student_dict2 = {'Harry': 5, 'Olivia': 6}
# student_dict3 = {'Nancy': 7, 'Perry': 9}
#
# # join three dictionaries
# student_dict = {**student_dict1, **student_dict2, **student_dict3}
# # printing the final Merged dictionary
# # print(student_dict)
# ------------------------------------------------------------------
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# d = dict(zip(keys,values))
# # (keys,values)
# print(d)
