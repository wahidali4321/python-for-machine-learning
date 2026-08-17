import numpy_p1 as np
import matplotlib.pyplot as plt

days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
temperature = np.array([31, 33, 30, 34, 35, 36, 32])

plt.plot(
    days,
    temperature,
    marker="o",
    color="red",
    linestyle="--",
    linewidth=2,
    markersize=8
)

plt.title("Weekly Temperature Monitor")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()