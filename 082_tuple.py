#Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined by enclosing the elements in parentheses ().
#Creating a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))

#a tuple can contain elements of different data types, including other tuples and lists. However, since tuples are immutable, you cannot modify their contents after they have been created. You can access the elements of a tuple using indexing and slicing, just like with lists.

# print(my_tuple[1])  # Output: 1


# just like lists, tuples allows duplicate values and maintain the order of elements. You can also use various built-in functions and methods to work with tuples, such as len(), count(), and index().

# example 2 

# fruits=("apple", "banana", "cherry", "apple", "banana")
# print(fruits)

# example 3

name=("John", "Doe", 30, "Engineer")
# print(len(name)) 
# print()
# print(type(name))


# example 4
# casting can be done with tuples

# classnames=["Math", "Science", "History"]
# classnames=tuple(classnames)
# classnames=list(classnames)
# classnames[2]="Geography"
# classnames=tuple(classnames)
# print(classnames[0:4])

# exmaple 5
# to change elements in a tuple, you start by converting it to a list, modifying the list, and then converting it back to a tuple.

# colors = ("red", "green", "blue")

# step 1: convert the tuple to a list
# colors=list(colors)

# step 2: modify the list
# colors[1]="yellow"
# colors.append("purple")
# colors.insert(0,"orange")
# colors.remove("blue")
# print(colors)

# step 3: convert the list back to a tuple
# colors=tuple(colors)
# print()
# print(colors)
# 


#looping through a tuple
# groceries = ("milk", "bread", "eggs", "cheese")
# for item in groceries:
    # print(item)


# joining tuples
# tuple1=(1, 2, 3)
# tuple2=(4, 5, 6)
# print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)


# tuple methods 

# there are only two built-in methods for tuples: count() and index(). The count() method returns the number of occurrences of a specified value in the tuple, while the index() method returns the index of the first occurrence of a specified value.

my_tuple = (1, 2, 3, 4, 5, 2, 2, 3, 2, 2, 2)
print(my_tuple.count(2))  
print(my_tuple.index(3)) 