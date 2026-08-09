import numpy as np
import matplotlib.pyplot as plt

boys_hours = np.array([2, 3, 4, 5, 6, 7])
boys_marks = np.array([50, 55, 62, 70, 78, 85])

girls_hours = np.array([2, 3, 4, 5, 6, 7])
girls_marks = np.array([55, 62, 68, 75, 82, 90])

plt.scatter(boys_hours, boys_marks,
            marker='o', s=100, color='blue', alpha=0.6,
            label="Boys")

plt.scatter(girls_hours, girls_marks,
            marker='*', s=100, color='red', alpha=0.6,
            label="Girls")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()