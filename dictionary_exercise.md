Here’s your improved version with **tips for every single question**, still clean and ready to use in **.md format**.

---

# 🐍 Python Dictionary Exercises (Beginner Level)

## 📘 General Guidelines

* Use correct Python syntax and indentation
* Always use `print()` to check your output
* Use dictionary methods like:

  * `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`
* Avoid hardcoding — use dictionary operations
* Add comments (`#`) to explain your logic
* Test your code with different values
* Keep your code simple and readable

---

## 🧠 Exercises with Tips

### 1.

Create a dictionary called `student` with keys: `name`, `age`, and `course`. Assign appropriate values and print the dictionary.
💡 **Tip:** Use curly braces `{}` and key-value pairs like `"name": "Sam"`.

---

### 2.

Access and print the value of `name` from the `student` dictionary.
💡 **Tip:** Use square brackets like `student["name"]`.

---

### 3.

Add a new key `grade` to the `student` dictionary with a value of `"A"`.
💡 **Tip:** Assign a value using `student["grade"] = "A"`.

---

### 4.

Update the `age` of the student to a new value.
💡 **Tip:** Reassign the value using the same key.

---

### 5.

Remove the `course` key from the dictionary.
💡 **Tip:** Use `.pop()` or `del`.

---

### 6.

Print all the keys in the dictionary.
💡 **Tip:** Use `.keys()`.

---

### 7.

Print all the values in the dictionary.
💡 **Tip:** Use `.values()`.

---

### 8.

Print all key-value pairs using a loop.
💡 **Tip:** Use `.items()` in a `for` loop.

---

### 9.

Check if the key `email` exists in the dictionary.
💡 **Tip:** Use `in` keyword like `"email" in student`.

---

### 10.

Create a dictionary of 3 countries and their capitals. Print each country with its capital.
💡 **Tip:** Loop through `.items()` to access both key and value.

---

### 11.

Create a dictionary `numbers` with values from 1–5. Calculate the sum of all values.
💡 **Tip:** Use `sum()` with `.values()`.

---

### 12.

Write a program to count how many times each letter appears in a word using a dictionary.
💡 **Tip:** Loop through the word and update counts using `dict[key] = dict.get(key, 0) + 1`.

---

### 13.

Create a dictionary where keys are numbers (1–5) and values are their squares.
💡 **Tip:** Use a loop or dictionary comprehension.

---

### 14.

Merge two dictionaries into one.
💡 **Tip:** Use `.update()` or `{**dict1, **dict2}`.

---

### 15.

Create a nested dictionary for 2 students with their names and scores.
💡 **Tip:** A dictionary inside another dictionary.

---

### 16.

Access a value from a nested dictionary.
💡 **Tip:** Use multiple keys like `dict["outer"]["inner"]`.

---

### 17.

Use `.get()` method to safely access a key that may not exist.
💡 **Tip:** `.get("key", "default value")` prevents errors.

---

### 18.

Remove the last inserted item using a dictionary method.
💡 **Tip:** Use `.popitem()`.

---

### 19.

Sort a dictionary by keys and print the result.
💡 **Tip:** Use `sorted(dict)` or `sorted(dict.items())`.

---

### 20.

Create a dictionary from two lists:

* One list of keys
* One list of values
  💡 **Tip:** Use `zip()` and `dict()`.

---

## 🧩 Bonus Challenge

Write a program that:

* Takes a sentence as input
* Counts how many times each word appears
* Stores the result in a dictionary

💡 **Tip:** Use `.split()` to break the sentence into words.

---

## ✅ Example Answer Format

```python
# Exercise 1
student = {
    "name": "Sam",
    "age": 20,
    "course": "Cybersecurity"
}

print(student)
```

---

If you want next step, I can:

* add **difficulty levels (easy → hard)**
* provide **full solutions**
* or convert this into a **test/exam paper for your class**
