import numpy as np
import matplotlib.pyplot as plt
House_size = np.array([800, 1000, 1200, 1500, 1800, 2000, 2500])
Price =np.array([120, 150, 180, 220, 280, 320, 400])
plt.scatter(House_size , Price , s=120 , color = "orange")
plt.title("House Size vs Price")
plt.grid(True)
plt.xlabel("House size")
plt.ylabel("Price")
plt.show()