import numpy as np
import matplotlib.pyplot as plt
Months = np.array(["Jan" , "Feb" , "Mar" , "April" , "May" , "Jun"])
Rainfall = np.array([20, 35, 28, 45, 40, 50])
plt.plot(Months , Rainfall , ls = '--' , color = "blue")
plt.show()