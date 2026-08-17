import numpy_p1 as np

arr = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

# Standard deviation of each column
column_std = np.std(arr, axis=0)

# Standard deviation of each row
row_std = np.std(arr, axis=1)

print("Array:")
print(arr)

print("\nStandard deviation of each column:")
print(column_std)

print("\nStandard deviation of each row:")
print(row_std)