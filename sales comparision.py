import numpy as np
import matplotlib.pyplot as plt
Months = np.array(["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun"])
sales = np.array([120, 150, 180, 160, 200, 220])
plt.subplot(1,2,1)
plt.plot(Months , sales , marker = 'o')
plt.title("Sales Comparison")
plt.grid(True)
plt.xlabel("Months")
plt.ylabel("sales")

Months = np.array(["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun"])
sales = np.array([11,22,33,44,55 , 66])

plt.subplot(1,2,2)
plt.plot(Months , sales , marker = 'o')
plt.title("Sales Comparison")
plt.grid(True)
plt.xlabel("Months")
plt.ylabel("sales")
plt.show()
