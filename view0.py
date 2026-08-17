import numpy_p1 as np
y = np.array([11,22,33,44,55,66,77])
x = y.view()
x[0] = 44
print(y)
print(x)