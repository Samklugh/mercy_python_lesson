# Set joins

# There are many ways to join sets in Python. Here are some of the most common methods:

# 1. Using the union() method:
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "grape", "melon"}

# set_union = set1.union(set2) 
 
# this will create a new set that contains all the unique items from both sets

set_union = set1 | set2 # this will also create a new set that contains all the unique items from both sets


print(set_union) 
# this will print {'apple', 'banana', 'cherry', 'orange', 'grape', 'melon'}

# NOTE: the | operator can also be used to perform a union of two sets, but it is not recommended because it can be less readable and may lead to confusion with the bitwise OR operator.

# multiple sets can be joined together using the union() method or the | operator, for example:
set3 = {"kiwi", "peach", "plum"}
set4 = {"pear", "pineapple", "watermelon"}
set5 = {"strawberry", "blueberry", "raspberry"}
set6 = {"blackberry", "cranberry", "grapefruit"}

set_union = set1.union(set2, set3, set4, set5, set6)
# or 
set_union = set1 | set2 | set3 | set4 | set5 | set6

print(set_union)


# 2. intersection() method:
# this will create a new set that contains only the items that are present in both sets
name= {"John", "Jane", "Jack"}
name2 = {"Jane", "Jack", "Jill"}
name_intersection = name.intersection(name2)
# or    
name_intersection = name & name2

print()
print(name_intersection) # this will print {'Jane', 'Jack'}


# 3. difference() method:
# this will create a new set that contains only the items that are present in the first set but not in the second set
name_difference = name.difference(name2)
# or
name_difference = name - name2

print()
print(name_difference) # this will print {'John'}



# 4. symmetric_difference() method:
# this will create a new set that contains only the items that are present in either set but not in both sets
name_symmetric_difference = name.symmetric_difference(name2)
# or
name_symmetric_difference = name ^ name2
print()
print(name_symmetric_difference) # this will print {'John', 'Jill'}