import numpy_p1 as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 35, 34, 36, 33]
plt.plot(days , temperature )
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()