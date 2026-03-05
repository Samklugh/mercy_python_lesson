# import matplotlib.pyplot as plt

# weight=[12.3, 45.6, 78.9, 23.4, 56.7]
# height=[1.2, 1.5, 1.8, 1.3, 1.6]

# plt.scatter(weight, height)
# plt.xlabel("Weight (kg)")
# plt.ylabel("Height (m)")
# plt.title("Weight vs Height")
# plt.show()


# name="mercy"
# age=26
# weight=55
# location="london"
# height=5.5

# multiple variable assignment /PACKING
name, age, weight, location, height = "mercy", 26, 55, "london", 5.5

print(f"My name is {name}, I am {age} years old, I weigh {weight} kg, I live in {location}, and I am {height} feet tall.")


# UNPACKING
choice=("red", "blue", "green")
color1, color2, color3 = choice
print(color1)