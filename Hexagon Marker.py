import numpy_p1 as np
import matplotlib.pyplot as plt
time = [0, 1, 2, 3, 4]
speed = [0, 20, 40, 60, 80]
plt.plot(time , speed , marker = 'h' , ms = 12 , mfc = 'pink')
plt.grid(True)
plt.show()