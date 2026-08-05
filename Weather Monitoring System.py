import numpy as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 35, 36, 34, 33]
plt.plot(days , temperature , marker = '*' , mfc = 'red' ,  color = 'orange' )
plt.grid(True)
plt.show()