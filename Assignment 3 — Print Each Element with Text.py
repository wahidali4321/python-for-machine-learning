import numpy_p1 as np
arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
for x in arr:
  for y in x:
    print("Element: " , y)