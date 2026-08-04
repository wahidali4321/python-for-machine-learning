import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5])
distance = np.array([0, 10, 25, 45, 70, 100])

plt.plot(time, distance)

plt.title("Distance Traveled Over Time")
plt.xlabel("Time (Hours)")
plt.ylabel("Distance (Kilometers)")

plt.show()