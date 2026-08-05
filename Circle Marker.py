import numpy as np
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
sales = [120, 150, 170, 160, 180]
plt.plot(days , sales , marker = 'o' , ms = 8 , color = "green")
plt.title("Circle Marker")
plt.xlabel("days")
plt.ylabel("sales")
plt.grid(True)
plt.show()