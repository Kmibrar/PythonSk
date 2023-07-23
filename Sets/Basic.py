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

