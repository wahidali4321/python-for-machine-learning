import numpy as np
import matplotlib.pyplot as plt

months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
rainfall = np.array([30, 45, 25, 60, 40])
plt.plot(months , rainfall , '*')
plt.title("Monthly Rainfall")
plt.xlabel("months")
plt.ylabel("Rainfall in mm")
plt.show()