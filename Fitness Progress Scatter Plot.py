import numpy_p1 as np
import matplotlib.pyplot as plt

days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
steps = np.array([5000, 6500, 7000, 6200, 8000, 9000, 7500])
calories = np.array([200, 260, 280, 250, 320, 370, 300])

plt.scatter(steps, calories, s=100, color="green", marker="o")

plt.title("Fitness Progress")
plt.xlabel("Daily Steps")
plt.ylabel("Calories Burned")
plt.grid(True)

plt.show()