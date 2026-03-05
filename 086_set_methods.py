# # set methods in python

# 1. add() method: This method is used to add an item to a set. If the item already exists in the set, it will not be added again.

# 2. update() method: This method is used to add multiple items to a set. It
# takes an iterable (like a list, tuple, or another set) as an argument and adds all the items from that iterable to the set.

# 3. remove() method: This method is used to remove an item from a set. If
# the item does not exist in the set, it will raise a KeyError.

# 4. discard() method: This method is used to remove an item from a set. If
# the item does not exist in the set, it will not raise an error.

# 5. pop() method: This method is used to remove and return an arbitrary item from a set. Since sets are unordered, you cannot predict which item will be removed.

# 6. clear() method: This method is used to remove all items from a set, but
# the set itself will still exist.

# 7. del keyword: This is used to delete the entire set from memory, making it no longer accessible.

# 8. union() method: This method is used to create a new set that contains all the unique items from both sets.

# 9. intersection() method: This method is used to create a new set that contains only the
# items that are present in both sets.

# 10. difference() method: This method is used to create a new set that contains only the items that are present in the first set but not in the second set.

# 11. symmetric_difference() method: This method is used to create a new set that contains only
# the items that are present in either set but not in both sets.

# 12. issubset() method: This method is used to check if one set is a subset of another set.

# 13. issuperset() method: This method is used to check if one set is a superset of another set.

# 14. isdisjoint() method: This method is used to check if two sets have no items in common.

# 15. copy() method: This method is used to create a shallow copy of a set.


# set functions in python 

# 16. frozenset() function: This function is used to create an immutable version of a set, called a frooze set. A frooze set cannot be modified after it is created, meaning you cannot add or remove items from it. However, you can perform set operations on frooze sets, such as union, intersection, difference, and symmetric difference.

# 17. len() function: This function is used to get the number of items in a set.

# 18. type() function: This function is used to get the type of a set, which will return <class 'set'> for a regular set and <class 'frozenset'> for a frooze set.