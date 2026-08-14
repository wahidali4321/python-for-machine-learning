import numpy as np
z = np.array([10, 20, 30, 40, 50])
y = z.view()
z[0] = 34
print(z)
print(y)