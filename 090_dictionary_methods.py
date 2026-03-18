            # DICTIONARY METHODS
# ****************************************

# 1. clear() - removes all items from the dictionary

# 2. copy() - returns a shallow copy of the dictionary    

# # 3. fromkeys() - creates a new dictionary from a sequence of keys and a value

# 4. get() - returns the value of the specified key

# # 5. items() - returns a view object that displays a list of dictionary's key-value tuple

# # 6. keys() - returns a view object that displays a list of all the keys in the dictionary

# # 7. pop() - removes the specified key and returns the corresponding value

# # 8. popitem() - removes the last inserted key-value pair from the dictionary and returns it as a tuple

# # # 9. setdefault() - returns the value of the specified key. If the key does not exist, insert the key with the specified value

# # 10. update() - updates the dictionary with the specified key-value pairs

# # 11. values() - returns a view object that displays a list of all the values in the dictionary


# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # Output: 1
print(my_dict.keys())     # Output: dict_keys(['a', 'b', 'c'])
print(my_dict.values())   # Output: dict_values([1, 2, 3])
my_dict.pop('b')         # Removes key 'b' and returns its value
print(my_dict)           # Output: {'a': 1, 'c': 3
my_dict.update({'d': 4}) # Adds key 'd' with value 4
print(my_dict)           # Output: {'a': 1, 'c': 3, 'd': 4}

