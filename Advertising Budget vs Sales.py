import numpy as np
import matplotlib.pyplot as plt
Advertising_budget = np.array([100, 200, 300, 400, 500, 600, 700])
Sales = np.array([20, 35, 45, 55, 70, 82, 95])
plt.scatter(Advertising_budget , Sales , marker= 'o' , s = 12 , color = "blue")
plt.title("Advertising Budget vs Sales")
plt.xlabel("Advertising_budge")
plt.ylabel("Sales")
plt.grid(True)
plt.show()