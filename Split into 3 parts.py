import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = np.array_split(numbers , 3)
print(newarr)