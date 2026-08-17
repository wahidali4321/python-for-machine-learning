import numpy_p1 as np
import matplotlib.pyplot as plt
Months = np.array(["jan" , "feb" , "mar" , "apr" , "may"])
sales = np.array([100, 120, 115, 140, 160])
plt.plot(Months , sales , ls = '--')
plt.title("Monthly Sales 💰")
plt.grid(True)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()