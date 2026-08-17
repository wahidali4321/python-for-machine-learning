import numpy_p1 as np
import matplotlib.pyplot as plt
price_A = [10, 20, 30, 40, 50, 60]
sales_A = [95, 85, 75, 65, 55, 45]
plt.scatter(price_A , sales_A , marker= '*' , label = "Product A")

price_B = [10, 20, 30, 40, 50, 60]
sales_B = [110, 100, 90, 78, 65, 52]
plt.scatter(price_B , sales_B , marker= '*' , label = "Product B")
plt.title("Product A vs Product B — Price & Sales")
plt.xlabel("Sales")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()