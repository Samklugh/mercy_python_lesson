# *******************
# Revision ID: 098
# *******************

# 1.  Lists

# a list is a collection of items that are "ordered and changeable". Lists are defined using square brackets [] and can contain elements of different data types. Here are some examples of how to create and manipulate lists in Python:

my_list = [1, 2, 3, 'four', 'five', 6.0] # creating a list with different data types
print(f"\n\nMy list: {my_list}")

my_list.append('seven') # adding an element to the end of the list
print(f"\n\nMy list after appending 'seven': {my_list}")

my_list.insert(0, 'zero') # adding an element at a specific index
print(f"\n\nMy list after inserting 'zero' at index 0: {my_list}")

my_list.remove(2) # removing an element by value
print(f"\n\nMy list after removing the value 2: {my_list}")

my_list.pop(3) # removing an element by index
print(f"\n\nMy list after popping the element at index 3: {my_list}") 

my_list[1] = 'two' # changing the value of an element at a specific index
print(f"\n\nMy list after changing the value at index 1 to 'two': {my_list}")



# 2.  Tuples

# a tuple is a collection of items that are "ordered and unchangeable". Tuples are defined using parentheses () and can contain elements of different data types. Here are some examples of how to create and manipulate tuples in Python:

my_tuple = (1, 2, 3, 'four', 'five', 6.0) # creating a tuple with different data types
print(f"\n\nMy tuple: {my_tuple}")

# tuples are immutable, so we cannot change their values or add/remove elements. However, we can access their elements using indexing and slicing:

print(f"\n\nThe first element of my tuple is: {my_tuple[0]}") # accessing the first element
print(f"\n\nThe last element of my tuple is: {my_tuple[-1]}") # accessing the last element
print(f"\n\nThe elements from index 1 to 3 of my tuple are: {my_tuple[1:4]}") # accessing a slice of the tuple  

# my_tuple[2] = 'three' # this will raise a TypeError because tuples are immutable

tuple1=list(my_tuple) # we can convert a tuple to a list to make it mutable
tuple1[2] = 'three' # now we can change the value at index 2
my_tuple=tuple(tuple1) # we can convert the list back to a tuple
print(f"\n\nMy tuple after changing the value at index 2 to 'three': {my_tuple}")

# 3.  Sets

# a set is a collection of items that are "unordered and unindexed". Sets are defined using curly braces {} and can contain elements of different data types. Here are some examples of how to create and manipulate sets in Python:

my_set = {1, 2, 3, 'four', 'five', 6.0} # creating a set with different data types
print(f"\n\nMy set: {my_set}")

my_set.add('seven') # adding an element to the set
print(f"\n\nMy set after adding 'seven': {my_set}")

# sets do not allow duplicate elements, so if we try to add an element that already exists in the set, it will not be added again:

my_set.add(2) # trying to add the value 2 again
print(f"\n\nMy set after trying to add the value 2 again: {my_set}")

# 4.  Dictionaries
# a dictionary is a collection of items that are "unordered and changeable". Dictionaries are defined using curly braces {} and consist of key-value pairs. Here are some examples of how to create and manipulate dictionaries in Python:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'} # creating a dictionary with key-value pairs
print(f"\n\nMy dictionary: {my_dict}")

my_dict['country'] = 'USA' # adding a new key-value pair to the dictionary
print(f"\n\nMy dictionary after adding a new key-value pair: {my_dict}")

my_dict['age'] = 31 # changing the value of an existing key
print(f"\n\nMy dictionary after changing the value of the 'age' key: {my_dict}")

# to print the value of a specific key in the dictionary, we can use the key as an index:

print(f"\n\nThe value of the 'name' key in my dictionary is: {my_dict['name']}")

# or 
print(f"\n\nThe value of the 'name' key in my dictionary is: {my_dict.get('name')}") # using the get() method to access the value of a key  

# to print all the keys in the dictionary, we can use the keys() method:
print(f"\n\nThe keys in my dictionary are: {my_dict.keys()}")

# to print all the values in the dictionary, we can use the values() method:
print(f"\n\nThe values in my dictionary are: {my_dict.values()}")

# to print all the key-value pairs in the dictionary, we can use the items() method:
print(f"\n\nThe key-value pairs in my dictionary are: {my_dict.items()}")
