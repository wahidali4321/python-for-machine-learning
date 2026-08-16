import numpy as np
marks = np.array([65, 70, 75])
marks1 = np.array([80, 85, 90])
arr = np.concatenate((marks , marks1))
print(arr)