# Tuple
# Tuples are ordered collections of heterogeneous data that are unchangeable.
# Heterogeneous means tuple can store variables of all types.Tuples are ordered collections
# of heterogeneous data that are unchangeable. Heterogeneous means tuple can store variables of all types.

# Tuple has the following characteristics

# Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion.
# It maintains the index value for each item.

# Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.

# Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;)
# and can be accessed through indexing and slicing.

# Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value

# Basic
# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
# Output (10, 20, 25.75)

# string tuple
string_tuple = ('Jessa', 'Emma', 'Kelly')
print(string_tuple)
# Output ('Jessa', 'Emma', 'Kelly')

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)
# Output ('Jessa', 30, 45.75, [25, 78])

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [23, 78]))
print(sample_tuple2)
# Output ('Jessa', 30, 45.75, [23, 78])


Home » Python » Tuples in Python
Tuples in Python
Updated on: April 9, 2021 | 4 Comments

In this article, you will learn how to use a tuple data structure in Python. Also, learn how to create, access, and modify a tuple in Python and all other operations we can perform on a tuple.

What is a Tuple
Tuples are ordered collections of heterogeneous data that are unchangeable. Heterogeneous means tuple can store variables of all types.

Tuple has the following characteristics

Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value.
Also See:

Python Tuple Exercise
Python Tuple Quiz
Summary of Tuple Operations
Python tuples
Python tuples
Table of contents
What is a Tuple
Creating a Tuple
Create a tuple with a single item
Packing and Unpacking
Length of a Tuple
Iterating a Tuple
Accessing items of a Tuple
Indexing
Negative Indexing
Slicing a tuple
Finding an item in a Tuple
Find within a range
Checking if an item exists
Adding and changing items in a Tuple
Modify nested items of a tuple
Removing items from a tuple
Using del keyword
By converting it into a List
Count the occurrence of an item in a tuple
Copying a tuple
Concatenating two Tuples
Using the + operator
Using the sum() function
Using the chain() function
Nested tuples
Use built-in functions with tuple
min() and max()
all()
any()
When to use Tuple?
Summary of tuples operations
Creating a Tuple
We can create a tuple using the two ways

Using parenthesis (): A tuple is created by enclosing comma-separated items inside rounded brackets.
Using a tuple() constructor: Create a tuple by passing the comma-separated items inside the tuple().
Example

A tuple can have items of different data type integer, float, list, string, etc;

# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
# Output (10, 20, 25.75)

# string tuple
string_tuple = ('Jessa', 'Emma', 'Kelly')
print(string_tuple)
# Output ('Jessa', 'Emma', 'Kelly')

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)
# Output ('Jessa', 30, 45.75, [25, 78])

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [23, 78]))
print(sample_tuple2)
# Output ('Jessa', 30, 45.75, [23, 78])
 Run
As we can see in the above output, the different items are added in the tuple like integer, string, and list.

# Create a tuple with a single item
# A single item tuple is created by enclosing one item inside parentheses followed by a comma. If the tuple time is a string enclosed within parentheses and not followed by a comma, Python treats it as a str type. Let us see this with an example.

# without comma
single_tuple = ('Hello')
print(type(single_tuple))
# Output class 'str'
print(single_tuple)
# Output Hello

# with comma
single_tuple1 = ('Hello',)
# output class 'tuple'
print(type(single_tuple1))
# Output ('Hello',)
print(single_tuple1)



Home » Python » Tuples in Python
Tuples in Python
Updated on: April 9, 2021 | 4 Comments

In this article, you will learn how to use a tuple data structure in Python. Also, learn how to create, access, and modify a tuple in Python and all other operations we can perform on a tuple.

What is a Tuple
Tuples are ordered collections of heterogeneous data that are unchangeable. Heterogeneous means tuple can store variables of all types.

Tuple has the following characteristics

Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value.
Also See:

Python Tuple Exercise
Python Tuple Quiz
Summary of Tuple Operations
Python tuples
Python tuples
Table of contents
What is a Tuple
Creating a Tuple
Create a tuple with a single item
Packing and Unpacking
Length of a Tuple
Iterating a Tuple
Accessing items of a Tuple
Indexing
Negative Indexing
Slicing a tuple
Finding an item in a Tuple
Find within a range
Checking if an item exists
Adding and changing items in a Tuple
Modify nested items of a tuple
Removing items from a tuple
Using del keyword
By converting it into a List
Count the occurrence of an item in a tuple
Copying a tuple
Concatenating two Tuples
Using the + operator
Using the sum() function
Using the chain() function
Nested tuples
Use built-in functions with tuple
min() and max()
all()
any()
When to use Tuple?
Summary of tuples operations
Creating a Tuple
We can create a tuple using the two ways

Using parenthesis (): A tuple is created by enclosing comma-separated items inside rounded brackets.
Using a tuple() constructor: Create a tuple by passing the comma-separated items inside the tuple().
Example

A tuple can have items of different data type integer, float, list, string, etc;

# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
# Output (10, 20, 25.75)

# string tuple
string_tuple = ('Jessa', 'Emma', 'Kelly')
print(string_tuple)
# Output ('Jessa', 'Emma', 'Kelly')

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)
# Output ('Jessa', 30, 45.75, [25, 78])

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [23, 78]))
print(sample_tuple2)
# Output ('Jessa', 30, 45.75, [23, 78])
 Run
As we can see in the above output, the different items are added in the tuple like integer, string, and list.

Create a tuple with a single item
A single item tuple is created by enclosing one item inside parentheses followed by a comma. If the tuple time is a string enclosed within parentheses and not followed by a comma, Python treats it as a str type. Let us see this with an example.

# without comma
single_tuple = ('Hello')
print(type(single_tuple))
# Output class 'str'
print(single_tuple)
# Output Hello

# with comma
single_tuple1 = ('Hello',)
# output class 'tuple'
print(type(single_tuple1))
# Output ('Hello',)
print(single_tuple1)

# As we can see in the above output the first time, we did not add a comma after the “Hello”. So the variable type was class str, and the second time it was a class tuple.




# Packing and Unpacking
# A tuple can also be created without using a tuple() constructor or enclosing the items inside the parentheses. It is called the variable “Packing.”
#
# In Python, we can create a tuple by packing a group of variables. Packing can be used when we want to collect multiple values in a single variable. Generally, this operation is referred to as tuple packing.
#
# Similarly, we can unpack the items by just assigning the tuple items to the same number of variables. This process is called “Unpacking.”
#
# Let us see this with an example.

# packing variables into tuple
tuple1 = 1, 2, "Hello"
# display tuple
print(tuple1)
# Output (1, 2, 'Hello')

print(type(tuple1))
# Output class 'tuple'

# unpacking tuple into variable
i, j, k = tuple1
# printing the variables
print(i, j, k)
# Output 1 2 Hello



# Length of a Tuple
# We can find the length of the tuple using the len() function.
# This will return the number of items in the tuple.

tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
# length of a tuple
print(len(tuple1))
# Output 6



# Iterating a Tuple
# We can iterate a tuple using a for loop Let us see this with an example.

# create a tuple
sample_tuple = tuple((1, 2, 3, "Hello", [4, 8, 16]))
# iterate a tuple
for item in sample_tuple:
    print(item)


#     ---------------------------------- Practice
a={}
# a = {1,2}
print(a)
print(type(a))


b = []
# b = [1,2]
print(b)
print(type(b))

c=()
# c = (1,2)
print(c)
print(type(c))

d={}
# d = {"a": 4}
print(d)
print(type(d))

#  ---------------------------------------------
# Empty set,list,tuple,dictionary


Home » Python » Sets in Python
Sets in Python
Updated on: July 19, 2022 | 16 Comments

In Python, a Set is an unordered collection of data items that are unique. In other words, Python Set is a collection of elements (Or objects) that contains no duplicate elements.

Unlike List, Python Set doesn’t maintain the order of elements, i.e., It is an unordered data set. So you cannot access elements by their index or perform insert operation using an index number.

In this tutorial, we will learn Set data structure in general, different ways of creating them, and adding, updating, and removing the Set items. We will also learn the different set operations.

Also See:

Python Set Exercise
Python Set Quiz
Python Sets
Python Sets
Characteristics of a Set

A set is a built-in data structure in Python with the following three characteristics.

Unordered: The items in the set are unordered, unlike lists, i.e., it will not maintain the order in which the items are inserted. The items will be in a different order each time when we access the Set object. There will not be any index value assigned to each item in the set.
Unchangeable: Set items must be immutable. We cannot change the set items, i.e., We cannot modify the items’ value. But we can add or remove items to the Set. A set itself may be modified, but the elements contained in the set must be of an immutable type.
Unique: There cannot be two items with the same value in the set.
Table of contents
Creating a Set
Create a set from a list
Creating a set with mutable elements
Empty set
Accessing items of a set
Checking if an item exists in Set
Find the length of a set
Adding items to a Set
Removing item(s) from a set
remove() vs discard()
Set Operations
Union of sets
Intersection of Sets
Intersection update
Difference of Sets
Difference update
Symmetric difference of Sets
Symmetric difference update
Copying a Set
Subset and Superset
find whether two sets are disjoint
Sort the set
Using Python built-in functions for Set
all() and any()
max() and min()
Frozen Set
When to use frozenset ?
Nested Sets
Set comprehension
When to use a Set Data structure?
Creating a Set
There are following two ways to create a set in Python.

Using curly brackets: The easiest and straightforward way of creating a Set is by just enclosing all the data items inside the curly brackets {}. The individual values are comma-separated.
Using set() constructor: The set object is of type class 'set'. So we can create a set by calling the constructor of class ‘set’. The items we pass while calling are of the type iterable. We can pass items to the set constructor inside double-rounded brackets.
Let’s see each one of them with an example.

# create a set using {}
# set of mixed types intger, string, and floats
sample_set = {'Mark', 'Jessa', 25, 75.25}
print(sample_set)
# Output {25, 'Mark', 75.25, 'Jessa'}

# create a set using set constructor
# set of strings
book_set = set(("Harry Potter", "Angels and Demons", "Atlas Shrugged"))
print(book_set)
# output {'Harry Potter', 'Atlas Shrugged', 'Angels and Demons'}

print(type(book_set))
# Output class 'set'
 Run
Note:

As we can see in the above example the items in the set can be of any type like String, Integer, Float, or Boolean. This makes a Set Heterogeneous i.e. items of different types can be stored inside a set.
Also, the output shows all elements are unordered.
Create a set from a list
Also, set eliminating duplicate entries so if you try to create a set with duplicate items it will store an item only once and delete all duplicate items. Let’s create a set from an iterable like a list. We generally use this approach when we wanted to remove duplicate items from a list.

Example

# list with duplicate items
number_list = [20, 30, 20, 30, 50, 30]
# create a set from a list
sample_set = set(number_list)

print(sample_set)
# Output {50, 20, 30}
#
# Creating a set with mutable elements
# You will get an error if you try to create a set with mutable elements like lists or dictionaries as its elements.

# set of mutable types
sample_set = {'Mark', 'Jessa', [35, 78, 92]}
print(sample_set)
# # Output TypeError: unhashable type: 'list' [35, 78, 92]

# Empty set
# When we don’t pass any item to the set constructor then it will create an empty set.
#
# empty_set = set()
# print(type(empty_set))
# # class 'set'
#  Run
# Note(always create empty SET AND dictionary where Set will create with Constructor.
# When the same object ‘person’ is created without any items inside the curly brackets
# then it will be created as a dictionary which is another built-in data structure in Python.
# So whenever you wanted to create an empty set always use the set() constructor.



# Accessing items of a set
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
for book in book_set:
    print(book)



# Checking if an item exists in Set
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
if 'Harry Potter' in book_set:
    print("Book exists in the book set")
else:
    print("Book doesn't exist in the book set")
# Output Book exists in the book set

# check another item which is not present inside a set
print("A Man called Ove" in book_set)
# Output False


# Find the length of a set
# To find the length of a Set, we use the len() method. This method requires one parameter to be passed, the set’s name whose size we need to find.

# create a set using set constructor
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
print(len(book_set))
# Output 3


# Adding items to a Set
book_set = {'Harry Potter', 'Angels and Demons'}
# add() method
book_set.add('The God of Small Things')
# display the updated set
print(book_set)
# Output {'Harry Potter', 'The God of Small Things', 'Angels and Demons'}

# update() method to add more than one item
book_set.update(['Atlas Shrugged', 'Ulysses'])
# display the updated set
print(book_set)
# Output {'The God of Small Things', 'Angels and Demons', 'Atlas Shrugged', 'Harry Potter', 'Ulysses'}




# Removing item(s) from a set
Method	Description
remove()	To remove a single item from a set. This method will take one parameter, which is the item to be removed from the set. Throws a keyerror if an item not present in the original set
discard()	To remove a single item that may or may not be present in the set. This method also takes one parameter, which is the item to be removed. If that item is present, it will remove it. It will not throw any error if it is not present.
pop()	To remove any random item from a set
clear()	To remove all items from the Set. The output will be an empty set
del set	Delete the entire set
Python Set methods to remove items
Let’s see an example to delete single or multiple items from a set.

Example

color_set = {'red', 'orange', 'yellow', 'white', 'black'}

# remove single item
color_set.remove('yellow')
print(color_set)
# Output {'red', 'orange', 'white', 'black'}

# remove single item from a set without raising an error
color_set.discard('white')
print(color_set)
# Output {'orange', 'black', 'red'}

# remove any random item from a set
deleted_item = color_set.pop()
print(deleted_item)

# remove all items
color_set.clear()
print(color_set)
# output set()

# delete a set
del color_set