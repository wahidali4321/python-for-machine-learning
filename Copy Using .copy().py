import numpy as np
arrs = np.array([5, 10, 15, 20, 25])
x = arrs.copy()
x[4] = 100
print(arrs)
print(x)