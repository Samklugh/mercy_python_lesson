````md
# Python Beginner Exercises

These exercises are designed for beginners learning Python fundamentals such as variables, strings, lists, conditionals, loops, and functions.

---

## Exercise 1 – User Greeting Program

### Task
Write a program that asks the user for their **name** and **age**, then prints a message like:

`Hello Samson, you are 25 years old.`

### Tips
- Use `input()` to collect user information.
- Store the values in variables.
- Use **f-strings** or string concatenation to format the output.
- Remember that `input()` returns a string.

Example hint:

```python
name = input("Enter your name: ")
````

---

## Exercise 2 – Even or Odd Checker

### Task

Write a program that asks the user to enter a number and tells them whether the number is **even or odd**.

### Tips

* Convert the user input to an integer using `int()`.
* Use the **modulus operator `%`**.
* If a number divided by 2 has a remainder of `0`, it is even.

Example hint:

```python
number % 2 == 0
```

---

## Exercise 3 – List of Favourite Foods

### Task

Create a list containing **five favourite foods** and print:

* The first food
* The last food
* The total number of foods in the list

### Tips

* Use Python **lists**.
* Access elements using **indexing**.
* Use `len()` to find the list length.

Example hint:

```python
foods = ["rice", "pizza", "apple"]
```

---

## Exercise 4 – Number Loop

### Task

Write a program that prints numbers from **1 to 10** using a loop.

Then print the **square of each number**.

Example output:

```
1 -> 1
2 -> 4
3 -> 9
```

### Tips

* Use a **for loop**.
* Use the `range()` function.
* Use `**` for powers.

Example hint:

```python
for i in range(1, 11):
```

---

## Exercise 5 – Word Counter

### Task

Ask the user to type a sentence.
Your program should display the **number of words in the sentence**.

Example:

```
Input: Python is fun to learn
Output: 5 words
```

### Tips

* Use the `split()` string method.
* `split()` converts a sentence into a list of words.
* Use `len()` to count the words.

Example hint:

```python
sentence.split()
```

---

## Exercise 6 – Simple Calculator

### Task

Create a program that asks the user for **two numbers** and prints:

* Sum
* Difference
* Product
* Division

Example output:

```
Sum: 15
Difference: 5
Product: 50
Division: 2
```

### Tips

* Convert inputs to numbers using `float()` or `int()`.
* Use arithmetic operators:

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | addition       |
| `-`      | subtraction    |
| `*`      | multiplication |
| `/`      | division       |

---

## Exercise 7 – Function to Check Largest Number

### Task

Write a function that takes **three numbers** and returns the **largest number**.

Example:

```
largest(4, 10, 6)
Output: 10
```

### Tips

* Use the `def` keyword to define a function.
* Use **if statements** to compare values.
* You can also explore the built-in `max()` function.

Example hint:

```python
def largest(a, b, c):
```

---

# Challenge (Optional)

Try modifying the exercises by:

* Adding **error handling** with `try` and `except`
* Using **loops** to repeat the program
* Converting some logic into **functions**

These modifications will help reinforce your Python skills.

```
```
