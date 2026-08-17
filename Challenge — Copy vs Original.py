import numpy_p1 as np
nu = np.array([10, 20, 30, 40, 50])
x = nu.copy()
x[0] = 999
nu[4] = 888
print(x)
print(nu)