# *********************
##    dictionaries   ##
# *********************

# a dictionary is a collection of key-value pairs, UNORDERED, CHANGEABLE, and INDEXED.

# example 1:
example_dictionary = {"one": 1, "two": 2, "three": 3, "four": 4}

# the key is always in a quotation mark and immediately followed by a colon and then the value. The key is always a string, while the value can be of any data type. 
# the keys in a dictionary must be unique, but the values can be duplicated.

# example 2:
student_info = {
    "name": "John Doe", 
    "age": 20, 
    "major": "Computer Science",
    "gpa": 3.5,
    "is_graduated": False,
    "courses": ["CS101", "CS102", "CS103"]
}


                # dataypes
# ****************************************

print(type(student_info)) # <class 'dict'>
print()


         # slcing keys and values
# ****************************************

househould_expenses = {
    "rent": 1200,   
    "utilities": 300,
    "groceries": 400,
    "transportation": 150,
    "entertainment": 200
}

rent_amount = househould_expenses["utilities"] # accessing the value of the key "utilities"
print("Rent amount:", rent_amount)
print()


                # changeable
# ****************************************
househould_expenses["transportation"] = 300 # changing the value of the key "transportation"
print("Updated household expenses:", househould_expenses)
print()



                # length of a dictionary
# ****************************************

num_of_expenses = len(househould_expenses) # getting the number of key-value pairs in the dictionary
print("Number of household expenses:", num_of_expenses)
print()



                # casting 
# ****************************************

family_members_age= (("mercy", 30), ("john", 35), ("susan", 25)) # a tuple of tuples
family_members_age_dict = dict(family_members_age) # casting the tuple of tuples to a dictionary
print("Family members age dictionary:", family_members_age_dict)
print()



         # accessing keys and values
# ****************************************

employer_info = {
    "company_name": "Tech Solutions Inc.",
    "location": "New York",
    "industry": "Information Technology",
    "number_of_employees": 500,
    "is_public": True
}

total_employees = employer_info["number_of_employees"]
print("Total number of employees:", total_employees)
print()


        # methods of a dictionary
# ****************************************

# using the get() method to access the value of a key
company_location = employer_info.get("location")
print("Company location:", company_location)
print()


# getting all the keys
keys=employer_info.keys()
print("All keys:", keys)
print()


# getting all the values
values=employer_info.values()
print("values:", values)
print()

# getting all the key-value pairs/items
items=employer_info.items()
print("All key-value pairs:", items)
print()




                # changing items
# ****************************************

alumni_info = {
    "name": "Jane Smith",   
    "graduation_year": 2015,
    "degree": "Bachelor of Arts",
    "major": "English Literature",
    "gpa": 3.8
}

alumni_info["gpa"] = 3.9 # changing the value of the key "gpa"  
print("Updated alumni information:", alumni_info)



        # update method
# ****************************************


alumni_info.update({"graduation_year": 2016}) 

# changing the value of the key "graduation_year" using the update() method
print("Updated alumni information:", alumni_info)


                # adding new items
# ****************************************
alumni_info["my_age"] = 30 # adding a new key-value pair to the dictionary
print("Updated alumni information with new item:", alumni_info)
print()


alumni_info.update({"my_hobby": "farting"}) # adding a new key-value pair to the dictionary using the update() method
print("Updated alumni information with new item:", alumni_info)


# removing from the dictionary

alumni_info.pop("my_hobby") # removing the key-value pair with the key "my_hobby" from the dictionary
print("Updated alumni information after removing an item:", alumni_info)
print()

alumni_info.popitem() # removing the last inserted key-value pair from the dictionary
print("Updated alumni information after removing the last item:", alumni_info)
print()

del alumni_info["my_age"] # removing the key-value pair with the key "my_age" from the dictionary using the del keyword
print("Updated alumni information after removing an item using del keyword:", alumni_info)
print() 

alumni_info.clear() # removing all key-value pairs from the dictionary
print("Updated alumni information after clearing the dictionary:", alumni_info) 
print() 