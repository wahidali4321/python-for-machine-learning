import numpy_p1 as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Variance of each column
column_var = np.var(arr, axis=0)

# Variance of each row
row_var = np.var(arr, axis=1)

print("Array:")
print(arr)

print("\nVariance of each column:")
print(column_var)

print("\nVariance of each row:")
print(row_var)