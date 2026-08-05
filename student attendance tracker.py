import numpy as np
import matplotlib.pyplot as plt
weeks = [1, 2, 3, 4, 5]
attendance = [90, 88, 95, 92, 96]
plt.plot(weeks , attendance , marker = 's' , ms = 12 , linewidth = 3)
plt.title("Student Attendence Tracker")
plt.xlabel("Weeks")
plt.ylabel('Attendance')
plt.show()