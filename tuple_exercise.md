
# Python Tuple Exercises (Beginner Level)

---

## Exercise 1: Create and Access a Tuple

Create a tuple named `fruits` with the following values:

```
"apple", "banana", "cherry", "mango"
```

* Print the entire tuple.
* Print the first item.
* Print the last item using negative indexing.


### Hint

* Tuples use parentheses `()`
* Indexing starts at `0`
* The last item can be accessed using `-1`

---

## Exercise 2: Tuple Length and Type

Create a tuple named `numbers` with the values:

```
10, 20, 30, 40, 50
```

* Print the length of the tuple.
* Print the data type of the tuple.

### Hint

* Use the `len()` function to get length.
* Use the `type()` function to check data type.

---

## Exercise 3: Tuple Slicing

Create a tuple called `colors`:

```
"red", "blue", "green", "yellow", "purple"
```

* Print the first three colors using slicing.
* Print the last two colors using slicing.

### Hint

* Slicing format: `tuple[start:end]`
* The `end` index is not included.
* You can use negative slicing like `tuple[-2:]`

---

## Exercise 4: Tuple Unpacking

Create a tuple:

```
person = ("John", 25, "London")
```

* Unpack the tuple into three variables: `name`, `age`, `city`
* Print each variable separately.

### Hint

* You can assign tuple values directly like this:

  ```
  a, b, c = my_tuple
  ```

* The number of variables must match the number of tuple items.

---

## Exercise 5: Convert Between Tuple and List

Create a tuple:

```
animals = ("dog", "cat", "lion")
```

* Convert the tuple into a list.
* Add `"tiger"` to the list.
* Convert the list back into a tuple.
* Print the final tuple.

### Hint

* Use `list()` to convert a tuple to a list.
* Use `tuple()` to convert a list back to a tuple.
* Remember: Tuples are immutable (cannot be changed directly).

---