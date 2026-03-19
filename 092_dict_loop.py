# DICTIONARY LOOP
# ****************************************

# You can loop through a dictionary using a for loop. When you loop through a dictionary, you can access the keys, values, or key-value pairs (items).

# looping through keys
student_info = {
    "name": "John Doe", 
    "age": 20, 
    "major": "Computer Science",
    "gpa": 3.5,
    "is_graduated": False,
    "courses": ["CS101", "CS102", "CS103"]
}

print("Looping through keys:")
for key in student_info.keys():
    print(key)


# looping through values
print("\nLooping through values:")
for value in student_info.values():
    print(value)


# looping through key-value pairs (items)
print("\nLooping through key-value pairs:")
for key, value in student_info.items():
    print(f"{key}: {value}")