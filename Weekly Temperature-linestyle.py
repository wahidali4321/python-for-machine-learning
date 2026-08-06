import numpy as np
import matplotlib.pyplot as plt
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
temperature = np.array([30, 32, 31, 34, 36, 35, 33])
plt.plot(days , temperature , ls = '-' , color = "blue")
plt.title("Weekly Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()