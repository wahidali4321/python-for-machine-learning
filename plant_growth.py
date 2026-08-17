import numpy_p1 as np
import matplotlib.pyplot as plt

days = np.array([1, 3, 5, 7, 9])
heights = np.array([5, 8, 12, 15, 18])

plt.plot(days, heights)

plt.title("Plant Growth Over Time")
plt.xlabel("Days")
plt.ylabel("Height (cm)")

plt.show()