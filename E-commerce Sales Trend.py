import numpy as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [1200, 1350, 1500, 1450, 1700, 2200, 2100]
plt.plot(days , sales , marker = 'o' , mfc = 'yellow' , mec = 'black' , ms = 10 , color = "blue")
plt.title("E-commerce Sales Trend")
plt.xlabel("days")
plt.ylabel("sales")
plt.grid(True)
plt.show()