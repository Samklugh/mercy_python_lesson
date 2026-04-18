# ***************************
# Built-in Modules in Python
# ***************************


# Python has a large standard library that includes many built-in modules that we can use in our programs. Some of the most commonly used built-in modules include: 
# 1. math: This module provides mathematical functions such as trigonometric functions, logarithmic functions, and constants like pi and e.
# 2. random: This module provides functions for generating random numbers and performing random operations.
# 3. datetime: This module provides classes for working with dates and times.
# 4. os: This module provides functions for interacting with the operating system, such as file and directory operations.
# 5. sys: This module provides functions for interacting with the Python interpreter, such as accessing command-line arguments and exiting the program.
# 6. re: This module provides functions for working with regular expressions.   

# We can import these built-in modules using the import statement, just like we do with our own modules. For example, to import the math module, we can do it as follows:





import math

factorial_of_5 = math.factorial(100)



print(f"Factorial of 5 is: {factorial_of_5}")



# ***************************
# MATH MODULE
# ***************************

# The math module provides a wide range of mathematical functions and constants. Some of the commonly used functions in the math module include:


number1=math.sqrt(500) # returns the square root of a number
print(f"\n\nThe square root of 500 is: {number1}")

number2=math.pow(2, 3) # returns the value of 2 raised to the power of 3
print(f"\n\nThe value of 2 raised to the power of 3 is: {number2}")

number3=math.sin(math.pi/2) # returns the sine of an angle in radians
print(f"\n\nThe sine of pi/2 is: {number3}")

number4=math.cos(0) # returns the cosine of an angle in radians
print(f"\n\nThe cosine of 0 is: {number4}")

number5=math.tan(math.pi/4) # returns the tangent of an angle in radians
print(f"\n\nThe tangent of pi/4 is: {number5}")

number6=math.log(100) # returns the natural logarithm of a number
print(f"\n\nThe natural logarithm of 100 is: {number6}")

number7=math.exp(2) # returns the value of e raised to the power of 2
print(f"\n\nThe value of e raised to the power of 2 is: {number7}")

number8=math.pi # returns the value of pi
print(f"\n\nThe value of pi is: {number8}")

number9=math.e # returns the value of e
print(f"\n\nThe value of e is: {number9}")

number10=math.ceil(4.2) # returns the smallest integer greater than or equal to a number
print(f"\n\nThe smallest integer greater than or equal to 4.2 is: {number10}")

number11=math.floor(4.7) # returns the largest integer less than or equal to a number
print(f"\n\nThe largest integer less than or equal to 4.7 is: {number11}")

number12=math.fabs(-5) # returns the absolute value of a number
print(f"\n\nThe absolute value of -5 is: {number12}")

number13=math.gcd(48, 18) # returns the greatest common divisor of two numbers
print(f"\n\nThe greatest common divisor of 48 and 18 is: {number13}")

number14=math.lcm(48, 18) # returns the least common multiple of two numbers
print(f"\n\nThe least common multiple of 48 and 18 is: {number14}")

number15=math.isqrt(16) # returns the integer square root of a number
print(f"\n\nThe integer square root of 16 is: {number15}")

number16=math.prod([1, 2, 3, 4]) # returns the product of all the elements in an iterable
print(f"\n\nThe product of all the elements in the list [1, 2, 3, 4] is: {number16}")

number17=math.comb(5, 2) # returns the number of ways to choose 2 items from a set of 5 items
print(f"\n\nThe number of ways to choose 2 items from a set of 5 items is: {number17}")

number18=math.perm(5, 2) # returns the number of ways to choose 2 items from a set of 5 items and arrange them in a specific order
print(f"\n\nThe number of ways to choose 2 items from a set of 5 items and arrange them in a specific order is: {number18}")

number19=math.dist([1, 2], [4, 6]) # returns the Euclidean distance between two points in a 2D space
print(f"\n\nThe Euclidean distance between the points (1, 2) and (4, 6) is: {number19}")

number20=math.hypot(3, 4) # returns the length of the hypotenuse of a right triangle given the lengths of the other two sides
print(f"\n\nThe length of the hypotenuse of a right triangle with sides of length 3 and 4 is: {number20}")

number21=math.copysign(-5, 1) # returns a float with the magnitude of the first argument and the sign of the second argument
print(f"\n\nThe value of copysign(-5, 1) is: {number21}")

number22=math.isclose(0.1 + 0.2, 0.3) # returns True if the two numbers are close to each other within a certain tolerance
print(f"\n\nIs 0.1 + 0.2 close to 0.3? {number22}")

number23=math.isnan(float('nan')) # returns True if the argument is NaN (Not a Number)
print(f"\n\nIs NaN (Not a Number) a number? {number23}")

number24=math.isinf(float('inf')) # returns True if the argument is positive or negative infinity
print(f"\n\nIs infinity a number? {number24}")

number25=math.isfinite(float('inf')) # returns True if the argument is a finite number
print(f"\n\nIs infinity a finite number? {number25}")

number26=math.modf(3.14) # returns the fractional and integer parts of a number as a tuple
print(f"\n\nThe fractional and integer parts of 3.14 are: {number26}")

number27=math.frexp(8) # returns the mantissa and exponent of a number as a tuple
print(f"\n\nThe mantissa and exponent of 8 are: {number27}")

number28=math.ldexp(0.5, 3) # returns the value of x * (2**i) where x is the first argument and i is the second argument
print(f"\n\nThe value of 0.5 * (2**3) is: {number28}")

number29=math.gamma(5) # returns the gamma function of a number
print(f"\n\nThe gamma function of 5 is: {number29}")

number30=math.lgamma(5) # returns the natural logarithm of the absolute value of the gamma function of a number
print(f"\n\nThe natural logarithm of the absolute value of the gamma function of 5 is: {number30}")

number31=math.erf(1) # returns the error function of a number
print(f"\n\nThe error function of 1 is: {number31}")

number32=math.erfc(1) # returns the complementary error function of a number
print(f"\n\nThe complementary error function of 1 is: {number32}")

number33=math.expm1(1) # returns the value of e raised to the power of x minus 1
print(f"\n\nThe value of e raised to the power of 1 minus 1 is: {number33}")

number34=math.log1p(1) # returns the natural logarithm of 1 plus a number
print(f"\n\nThe natural logarithm of 1 plus 1 is: {number34}")

number35=math.log10(100) # returns the base-10 logarithm of a number
print(f"\n\nThe base-10 logarithm of 100 is: {number35}")

number36=math.log2(8) # returns the base-2 logarithm of a number
print(f"\n\nThe base-2 logarithm of 8 is: {number36}")

number37=math.factorial(5) # returns the factorial of a number
print(f"\n\nThe factorial of 5 is: {number37}")

number38=math.comb(5, 2) # returns the number of ways to choose 2 items from a set of 5 items
print(f"\n\nThe number of ways to choose 2 items from a set of 5 items is: {number38}")

number39=math.perm(5, 2) # returns the number of ways to choose 2 items from a set of 5 items and arrange them in a specific order
print(f"\n\nThe number of ways to choose 2 items from a set of 5 items and arrange them in a specific order is: {number39}")

math.pi # returns the value of pi
print(f"\n\nThe value of pi is: {math.pi}")

math.e # returns the value of e
print(f"\n\nThe value of e is: {math.e}")

math.inf # returns positive infinity
print(f"\n\nThe value of positive infinity is: {math.inf}")

math.nan # returns NaN (Not a Number)
print(f"\n\nThe value of NaN (Not a Number) is: {math.nan}")

math.tau # returns the value of tau (2 * pi)
print(f"\n\nThe value of tau (2 * pi) is: {math.tau}")

math.nextafter(1.0, 2.0) # returns the next floating-point value after x towards y
print(f"\n\nThe next floating-point value after 1.0 towards 2.0 is: {math.nextafter(1.0, 2.0)}")

math.ulp(1.0) # returns the value of the least positive normal floating-point number that is greater than x
print(f"\n\nThe value of the least positive normal floating-point number that is greater than 1.0 is: {math.ulp(1.0)}")

math.remainder(10, 3) # returns the remainder of x divided by y
print(f"\n\nThe remainder of 10 divided by 3 is: {math.remainder(10, 3)}")

math.fmod(10, 3) # returns the remainder of x divided by y, but with a different sign than the built-in modulus operator
print(f"\n\nThe remainder of 10 divided by 3 using fmod is: {math.fmod(10, 3)}")


# math.min(1, 2, 3) 
# returns the smallest of the input values
# print(f"\n\nThe smallest of the input values 1, 2, and 3 is: {math.min(1, 2, 3)}")

# math.max(1, 2, 3) 
# returns the largest of the input values
# print(f"\n\nThe largest of the input values 1, 2, and 3 is: {math.max(1, 2, 3)}")

math.fsum([1, 2, 3]) # returns the sum of the input values as a float
print(f"\n\nThe sum of the input values 1, 2, and 3 is: {math.fsum([1, 2, 3])}")




