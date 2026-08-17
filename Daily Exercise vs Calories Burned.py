import numpy_p1 as np
import matplotlib.pyplot as plt
Exercise_minutes = np.array([10, 20, 30, 40, 50, 60, 70])
calories = np.array([80, 150, 220, 300, 380, 450, 530])
plt.scatter(Exercise_minutes , calories , marker = 'o' , s = 100 , color = "red")
plt.grid(True)
plt.show()