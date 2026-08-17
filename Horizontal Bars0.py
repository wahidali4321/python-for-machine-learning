import numpy_p1 as np
import matplotlib.pyplot as plt

x = np.array(["A" , 'B' , 'C' , 'D'])
y = np.array([11,22,33,44])
plt.barh(x , y)
plt.show()