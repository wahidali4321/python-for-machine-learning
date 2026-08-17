import numpy_p1 as np
arr = np.array([
    1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12,
    13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24
])
re = arr.reshape(4,6)
are = re.reshape(6,4)
print(re)
print(are)
print(re.shape)
print(are.shape)