import numpy_p1 as np
import matplotlib.pyplot as plt
height = [150, 155, 160, 165, 170, 175, 180]
weight = [45, 50, 55, 60, 65, 72, 78]
plt.scatter(height , weight , marker = 'o')
plt.title('Height vs Weight')
plt.xlabel("Height in cm")
plt.ylabel("Weight in kg")
plt.show()