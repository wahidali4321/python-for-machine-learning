import numpy as np
import matplotlib.pyplot as plt

weeks = np.array([1, 2, 3, 4, 5, 6])
weight = np.array([78, 77, 76, 75, 74, 73])

plt.plot(
    weeks,
    weight,
    marker="o",
    color="blue",
    linestyle="-",
    linewidth=2,
    markersize=8
)

plt.title("Fitness Progress")
plt.xlabel("Weeks")
plt.ylabel("Weight (kg)")
plt.grid(True)

plt.show()