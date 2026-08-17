import numpy_p1 as np
import matplotlib.pyplot as plt

days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

Daily_steps = np.array([5000, 6500, 7000, 6200, 8000, 9000, 7500])
Calories_burned = np.array([300, 350, 400, 320, 450, 500, 420])
Hours_of_sleep = np.array([7, 8, 6, 7, 8, 9, 8])
Water_intake = np.array([6, 7, 8, 6, 9, 10, 8])

# Plot 1 - Daily Steps
plt.subplot(2, 2, 1)
plt.plot(days, Daily_steps, marker='o')
plt.title("Daily Steps")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.grid(True)

# Plot 2 - Calories Burned
plt.subplot(2, 2, 2)
plt.plot(days, Calories_burned, marker='o')
plt.title("Calories Burned")
plt.xlabel("Days")
plt.ylabel("Calories")
plt.grid(True)

# Plot 3 - Hours of Sleep
plt.subplot(2, 2, 3)
plt.plot(days, Hours_of_sleep, marker='o')
plt.title("Hours of Sleep")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.grid(True)

# Plot 4 - Water Intake
plt.subplot(2, 2, 4)
plt.plot(days, Water_intake, marker='o')
plt.title("Water Intake")
plt.xlabel("Days")
plt.ylabel("Glasses")
plt.grid(True)

plt.tight_layout()
plt.show()