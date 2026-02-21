# list methods

# 1. append() method: it adds an item to the end of the list
countries=["Nigeria", "Ghana", "Kenya"]
countries.append("South Africa")
print(countries)
print()

# 2. insert() method: it adds an item at a specified index
countries.insert(1, "Egypt")
print(countries)
print()

# 3. extend() method: it adds items from another list to the end of the list
african_countries=["Nigeria", "Ghana", "Kenya"] 
european_countries=["France", "Germany", "Italy", "Germany"]
african_countries.extend(european_countries)
print(african_countries)
print()

# 4. pop() method: it removes an item at a specified index and returns it
removed_country=african_countries.pop(2)    
print(african_countries)
print(removed_country)
print()

# 5. remove() method: it removes the first occurrence of a specified value
african_countries.remove("Germany") 
print(african_countries)

# 6. delete() method: it removes an item at a specified index without returning it
del african_countries[3]
print(african_countries)
print()

# 7. clear() method: it removes all items from the list
african_countries.clear()
print(african_countries)

# 8. count() method: it returns the number of occurrences of a specified value in the list

european_countries=["France", "Germany", "Italy", "Germany"]
germany_count=european_countries.count("Germany")
print(germany_count)
print()

# 9. index() method: it returns the index of the first occurrence of a specified value in the list
italy_index=european_countries.index("Italy")
print(italy_index)
print()

# 10. sort() method: it sorts the items of the list in ascending order
european_countries.sort()
print(european_countries)
print()

# 11. reverse() method: it reverses the order of the items in the list
european_countries.reverse()
print(european_countries)

# 12. copy() method: it returns a shallow copy of the list
african_countries=["Nigeria", "Ghana", "Kenya"]
african_countries_copy=african_countries.copy()
print(african_countries_copy)
print()

# 13. join() method: it concatenates the items of a list into a single string, with a specified separator
countries=["Nigeria", "Ghana", "Kenya"]
countries_string=", ".join(countries)
print(countries_string)
print()
    
# 14. split() method: it splits a string into a list of substrings based on a specified separator
countries_string="Nigeria, Ghana, Kenya"
countries_list=countries_string.split(", ")
print(countries_list)
print()

# 15. len() function: it returns the number of items in the list
countries=["Nigeria", "Ghana", "Kenya"]
countries_length=len(countries)
print(countries_length)
print()


