import numpy as np
import matplotlib.pyplot as plt

# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([22, 33, 44, 55, 66, 77])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()