import numpy as np
import matplotlib.pyplot as plt

Age = np.array([10, 12, 14, 16, 18, 20, 22, 25])
Screen_time = np.array([5, 6, 5.5, 7, 8, 7.5, 6, 5])

plt.scatter(Age, Screen_time, marker='o', s=100, color='blue', alpha=1)

plt.title("Age vs Daily Screen Time")
plt.xlabel("Age")
plt.ylabel("Screen Time (hours)")
plt.grid(True)

plt.show()