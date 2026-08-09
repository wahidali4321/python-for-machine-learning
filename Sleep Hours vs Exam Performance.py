import numpy as np
import matplotlib.pyplot as plt
Sleep_hours = np.array([4, 5, 6, 7, 8, 9, 10])
Performance = np.array([55, 60, 65, 72, 80, 85, 88])
plt.scatter(Sleep_hours , Performance , marker= '*' , s=12 , color = "red")
plt.xlabel('Sleep hours')
plt.ylabel("Performance")
plt.title("Sleep Hours vs Exam Performance")
plt.grid(True)
plt.show()