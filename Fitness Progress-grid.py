import numpy_p1 as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [5000, 6500, 7000, 6200, 8000, 9000, 7500]
plt.plot(days , steps , marker = 'o')
plt.grid(axis= 'y')
plt.title("Fitness Progress")
plt.show()