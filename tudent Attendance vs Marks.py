import numpy_p1 as np
import matplotlib.pyplot as plt
Attendance = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100])
Marks = np.array([45, 50, 55, 62, 68, 75, 82, 90, 95])
plt.scatter(Attendance , Marks , s=120 , alpha= 0.5)
plt.ylabel("Marks")
plt.xlabel("Attendance")
plt.title("student attendance vs marks")
plt.grid(True)
plt.show()