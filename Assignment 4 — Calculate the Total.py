import numpy_p1 as np

arr = np.array([
    [5, 10, 15],
    [20, 25, 30]
])

total = 0

for row in arr:
    for x in row:
        total = total + x

print("Total:", total)