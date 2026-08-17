import numpy_p1 as np
import matplotlib.pyplot as plt
dataset = np.array([1,2,3,4,5,6,7,8])
plt.plot(dataset , marker = 'o' ,ms = 12 ,  mfc = 'red' , mec = 'red' , color = 'blue')
plt.title("dataset of numbers ")
plt.xlabel("dataset")
plt.grid(True)
plt.show()