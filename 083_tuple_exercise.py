# Question 1:

# fruits= ("apple", "banana", "cherry", "mango")

# print(fruits)

# first item
# print(fruits[0])
# last item
# print(fruits[-1])


# Question 2:
# numbers= (10, 20, 30, 40, 50)
# print(len(numbers))
# print(type(numbers))

# Question 3:
# colors=("red", "blue", "green", "yellow", "purple")
# print(colors[:3])
# print(colors[-2:])

# Question 4:
# unpacking a tuple

# main tuple variable
# person = ("John", 25, "London")

# unpacked variables
# name, age, city = person

# print(person)
# 
# print()
# 
# print("------Unpacked--------")
# print(name)
# print(age)
# print(city)


# question 5:
animals = ("dog", "cat", "lion")

# convert the tuple to a list
animals_list = list(animals)
animals_list.append("tiger")

# convert the list back to a tuple
animals = tuple(animals_list)

print(animals)