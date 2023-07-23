# Dictionary= a collection of {key: value} pairs ordered and changeable. No Duplicates
# Dictionary= Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])

# Creating a dictionary
# 1 curly brackets
# person = {"name": "Jessa", "country": "USA", "telephone": 1178}
# print(person)

# 2 dict() constractor
# person = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
# print(person)

# 3 sequence
# person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
# print(person)

# create dictionary with mixed keys keys
# first key is string and second is an integer
# sample_dict = {"name": "Jessa", 10: "Mobile"}
# print(sample_dict)

# create dictionary with value as a list
# person = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
# print(person)

# list of methods DIR
dict ={"Pakistan": "Islamabad "}
print(dir(dict))
# ['  '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
# '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(help(dict))