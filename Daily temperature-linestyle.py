import numpy as np
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 35, 34]

plt.plot(
    days,
    temperature,
    ls='-',          # Line style
    color='blue',    # Line color
    lw=2             # Line width
)

plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()