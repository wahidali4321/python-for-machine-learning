import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([1, 2, 3, 4, 5, 6, 7, 8])

plt.plot(
    dataset,
    marker='o',
    ms=12,
    mfc='red',
    mec='red',
    color='blue',
    linewidth=3
)

plt.title("Dataset of Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)

plt.show()