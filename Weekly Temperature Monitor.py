import numpy as np
import matplotlib.pyplot as plt
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
temperature = np.array([31, 33, 30, 34, 35, 36, 32])
plt.plot(days , temperature)
plt.title("Weekly Temperature Monitor")
plt.xlabel("Days")
plt.ylabel("temperature in 0C")
plt.show()