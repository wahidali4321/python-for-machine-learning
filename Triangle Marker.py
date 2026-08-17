import numpy_p1 as np
import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5]
study = [2, 3, 5, 4, 6]
plt.plot(hours , study , marker = '^' , ms = 12 , color = 'red')
plt.grid(True)
plt.show()