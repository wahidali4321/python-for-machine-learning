import numpy as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [120, 150, 180, 160, 220, 300, 250]
plt.plot(days , visitors)
plt.title("Website Visitors")
plt.xlabel("days")
plt.ylabel("visitors")
plt.grid(axis= 'y')
plt.show()