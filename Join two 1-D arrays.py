import numpy_p1 as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Join arr1 and arr2 using np.concatenate()
arr = np.concatenate((arr1 , arr2))
print(arr)