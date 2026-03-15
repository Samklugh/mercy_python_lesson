import math
import pandas as pd
import matplotlib.pyplot as plt

age =[23, 45, 12, 67, 34, 89, 22, 56, 78, 90]

salary = [50000, 60000, 45000, 80000, 55000, 75000, 48000, 90000, 65000, 70000]

salary_age_df = pd.DataFrame({"Age": age, "Salary": salary})
salary_age_df.plot(x="Age", y="Salary", kind="line", marker="o")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


average_age = sum(age) / len(age)
average_salary = sum(salary) / len(salary)

print("Average Age:", average_age)
print("Average Salary:", average_salary)

min_age = min(age)
max_age = max(age)

print("Minimum Age:", min_age)
print("Maximum Age:", max_age)

age2=5

agesqr=math.sqrt(age2)
print("Square root of age2:", agesqr)


agefct=math.factorial(age2)
print("Factorial of age2:", agefct)

agepwr=math.pow(age2, 3)
print("age2 raised to the power of 3:", agepwr)


