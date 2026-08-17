import numpy_p1 as np
import matplotlib.pyplot as plt
Products = np.array(["Laptop" , "Mobile" , "Tablet"])
Sales = np.array([120, 250, 180])
plt.bar(Products , Sales)
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()