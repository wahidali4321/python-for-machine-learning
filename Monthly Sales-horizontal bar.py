import numpy_p1 as np
import matplotlib.pyplot as plt
Months = np.array(["jan" , "feb" , "march" , "aprail" , "may" , "jun"])
sales = np.array([120, 150, 100, 180, 200 , 200])
plt.barh(Months , sales)
plt.title("Monthly Sales")
plt.show()