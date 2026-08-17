import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
newarr = np.array_split(arr , 2)
print(newarr)