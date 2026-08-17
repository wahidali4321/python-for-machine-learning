import numpy_p1 as np
import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [31, 33, 30, 34, 32]
plt.plot(days , temperature , marker = 'D' ,ms = 10 , mec = "orange" )
plt.title("Daily Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()
