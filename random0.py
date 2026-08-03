import random as rd
import numpy as np

numbers = []

for i in range(100):
    num = rd.randint(1, 100)
    numbers.append(num)

print("Random numbers:")
print(numbers)

x = np.std(numbers)
print("\nStandard Deviation:", x)