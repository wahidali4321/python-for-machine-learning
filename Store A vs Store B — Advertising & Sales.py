import numpy as np
import matplotlib.pyplot as plt
advertising_A = [10, 20, 30, 40, 50, 60]
sales_A = [100, 125, 150, 180, 210, 240]
plt.scatter(advertising_A , sales_A , marker= 's' , label = "Group A" , color = "green")

advertising_B = [10, 20, 30, 40, 50, 60]
sales_B = [90, 115, 145, 165, 195, 225]
plt.scatter(advertising_B , sales_B , marker= 's' , label = "Group B" , color= "yellow")
plt.title("Store A vs Store B — Advertising & Sales")
plt.xlabel("Advertising")
plt.ylabel("sales")
plt.grid()
plt.legend()
plt.show()