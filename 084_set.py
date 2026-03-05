# sets in python are unordered collections of unique items (you cant access them using indexing). They are defined using curly braces {} or the set() constructor. Sets are mutable, meaning you can add or remove items from them, but they do not allow duplicate values.

# animal={"dog", "fish", "goat", "cat", "dog"}
# print(animal) # this will print the set of unique animals, duplicates will be removed

# print(animal[1]) # this will raise an error because sets are unordered and do not support indexing

# NOTE 
# 1. True and 1 is considered the same value:
# my_set = {1, 2, 3, True}
# print(my_set) # this will print {1, 2, 3} because True is considered the same as 1 in a set

# 2. False and 0 is considered the same value:
# my_set = {0, 1, 2, False}
# print(my_set) # this will print {0, 1, 2} because False is considered the same as 0 in a set


# checking lenth and type of a set
# my_set = {"apple", "banana", "cherry"}
# print(len(my_set)) # this will print 3
# print(type(my_set)) # this will print <class 'set'>


# converting a list to a set
# my_list = [1, 2, 3, 4, 4, 4, 5, 5]
# my_set = set(my_list)

# print(my_set) # this will print {1, 2, 3, 4, 5} because sets only store unique values, duplicates will be removed



# adding items to a set

# 1. Using the add() method:

my_set = {"apple", "banana", "cherry"}
my_set.add("orange") # this will add "orange" to the set
# print(my_set) # this will print {'apple', 'banana', 'cherry', 'orange'}

# 2. Using the update() method:
my_set.update(["grape", "melon"]) # this will add "grape" and "melon" to the set    
# print(my_set) # this will print {'apple', 'banana', 'cherry', 'orange', 'grape', 'melon'}





# removing items from a set
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

# thisset.discard("banana") # this will also remove banana from the set, but it will not raise an error if the item is not found in the set

# print(thisset)



# we can also use the pop() method to remove an arbitrary item from the set, but since sets are unordered, we cannot predict which item will be removed.

# we can use the clear() method to remove all items from the set, but the set itself will still exist.

# we can use the del keyword to delete the entire set, but this will remove the set from memory and it will no longer be accessible.



# looping through a set
animals = {"dog", "cat", "lion"}
for elements in animals:
    print(elements) # this will print each animal in the set, but the order is not guaranteed since sets are unordered