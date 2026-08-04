import numpy as np
import matplotlib.pyplot as plt
heights = [150, 155, 160, 162, 165, 168, 170, 172, 175, 178,
           180, 182, 185, 188, 190]

count , bin , patches = plt.hist(heights , bins= 6)
print("Histogram count " , count)
print("Bin edges : " , bin)
plt.show()