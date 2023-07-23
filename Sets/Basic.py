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