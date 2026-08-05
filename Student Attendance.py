import numpy as np
import matplotlib.pyplot as plt
days = np.array([1, 2, 3, 4, 5])
attendance = np.array([25, 28, 27, 30, 29])
plt.plot(days , attendance , 'o')
plt.title("Weekly Attendance")
plt.xlabel("days")
plt.ylabel("attendance")
plt.show()