import numpy_p1 as np
import matplotlib.pyplot as plt

weeks = np.array([1, 2, 3, 4, 5])
weight = np.array([78, 77, 76, 75, 74])

plt.plot(
    weeks,
    weight,
    marker='^',          # Triangle marker
    mfc='cyan',          # Marker face color
    mec='black',         # Marker edge color
    markersize=10,
    color='blue',        # Line color
    linewidth=2
)

plt.title("Fitness Progress")
plt.xlabel("Weeks")
plt.ylabel("Weight (kg)")
plt.grid(True)

plt.show()