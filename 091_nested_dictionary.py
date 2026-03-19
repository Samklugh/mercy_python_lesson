# NESTED DICTIONARY
# *****************************************

# A nested dictionary is a dictionary that contains another dictionary as a value. It allows you to store and organize data in a hierarchical structure.


school_info = {
    "school_name": "Greenwood High School",
    "location": "New York",
    "students": {
        "student1": {
            "name": "Alice",
            "age": 15,
            "grade": 10
        },
        "student2": {
            "name": "Bob",
            "age": 16,
            "grade": 11
        }
    },
    "teachers": {
        "teacher1": {
            "name": "Mr. Smith",
            "subject": "Math"
        },
        "teacher2": {
            "name": "Ms. Johnson",
            "subject": "English"
        }
    }
}


print("School Information:", school_info["students"])  # Output: Alice