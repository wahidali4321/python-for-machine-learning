import numpy_p1 as np
import matplotlib.pyplot as plt
Cities = np.array(["peshawar" , "karachi" , "lahore" , "quetta" ])
population = np.array([2.0, 13.0, 20.0, 1.2])
plt.bar(Cities , population)
plt.show()
