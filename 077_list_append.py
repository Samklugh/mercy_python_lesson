# List revision

# list creation:
name=["John", "Jane", "Doe"]
print(type(name))

# slicing and indexing:
print(name[0])
print(name[1:3])

# changing list items:
name[0]="Mercy"
print(name)

# reversing a list:
print(name[::-1])

# list can contain a list as an item:
print()
name=["John", "Jane", "Doe", ["Mercy", "Grace"]]
print(name[3])
print(name[3][1])
print()

# length of a list 
print(len(name))

# WAYS OF CHANGING A LIST:

# 1. append() method: it adds an item to the end of the list
print()
name=["John", "Jane", "Doe", ["Mercy", "Grace"]]
name.append("Smith")
print(name)
print()

# 2. insert() method: it adds an item at a specified index
name.insert(1, "SAMSON")
print(name)
print()

# 3. extend() method: it adds items from another list to the end of the list
fruits=["apple", "banana", "orange"]
snacks=["chips", "cookies", "popcorn"]
fruits.extend(snacks)
print(fruits)
print()

# 4. concatenation: it combines two lists to create a new list
list1=[1, 2, 3]
list2=[4, 5, 6]
list3=list1 + list2 
print(list3)



# REMOVING FROM A LIST 
# 1. pop() method: it removes an item at a specified index and returns it
print()
name=["John", "Jane", "Doe", ["Mercy", "Grace"]]
removed_item=name.pop(1)
print(name)
print(removed_item)
print()

# 2. remove() method: it removes the first occurrence of a specified value
name.remove("Doe")
print(name)

# 3. del statement: it removes an item at a specified index or the entire list
print()
del name[0]
print(name)

# 4. clear() method: it removes all items from the list
print()
name.clear()
print(name)
