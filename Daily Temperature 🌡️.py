import numpy as np
import matplotlib.pyplot as plt
Days = np.array(["mon" , "tue" , "wed" , "thu" , "fri" ])
Temperature = np.array([30, 32, 31, 35, 34])
plt.plot(Days , Temperature , )
plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()