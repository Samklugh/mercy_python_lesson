student_info = {
    "name": "John Doe", 
    "age": 20, 
    "major": "Computer Science",
    "gpa": 3.5,
    "is_graduated": False,
    "courses": ["CS101", "CS102", "CS103"]
}

student_info.popitem() # removes the last inserted key-value pair and returns it
print("Updated student info:", student_info)
