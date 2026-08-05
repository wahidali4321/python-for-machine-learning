import numpy as np
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
temperature = [22, 24, 28, 31, 35]
plt.plot(months , temperature , marker = 's' , mfc = 'yellow' , mec = 'black' , color = "blue")
plt.show()