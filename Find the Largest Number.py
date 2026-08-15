import numpy as np

arr = np.array([45, 12, 78, 34, 90, 23])

largest = arr[0]

for x in arr:
    if x > largest:
        largest = x

print("Largest number:", largest)