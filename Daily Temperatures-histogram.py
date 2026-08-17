import numpy_p1 as np
import matplotlib.pyplot as plt
temperature = [28, 29, 30, 31, 32, 33, 34, 35,
               31, 30, 29, 28, 32, 33, 34]
count , bin , patches = plt.hist(temperature , bins= 5 , edgecolor="black" )
print("Total count is : " , count)
plt.title("Temperature")
plt.xlabel("numbers")
plt.ylabel("temperature")
plt.show()