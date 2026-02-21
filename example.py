import matplotlib.pyplot as plt

weight=[12.3, 45.6, 78.9, 23.4, 56.7]
height=[1.2, 1.5, 1.8, 1.3, 1.6]

plt.scatter(weight, height)
plt.xlabel("Weight (kg)")
plt.ylabel("Height (m)")
plt.title("Weight vs Height")
plt.show()