import numpy_p1 as np
import matplotlib.pyplot as plt
days = np.array(["mon" , "tue" , "wed" , "thur" , "fri" , "sat" , "sun"])
Temperatures = np.array([30, 31, 29, 33, 35, 34, 32])
plt.plot(days , Temperatures , ls = '-')
plt.show()