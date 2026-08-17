import numpy_p1 as np

arr = np.arange(1, 21)

parts = np.array_split(arr, 6)

for part in parts:
    print(part)