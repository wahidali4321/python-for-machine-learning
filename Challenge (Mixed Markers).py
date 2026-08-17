import numpy_p1 as np
import matplotlib.pyplot as plt
dataset = np.array([1,2,3,4,5,6,7,8,9,10])
plt.plot(dataset , marker = 'o' , ms = 14 , mfc = "black" , mec = "red" , linewidth = 3 , color = 'red')
plt.title("Challenge (Mixed Markers)")
plt.xlabel("numbers")
plt.ylabel("dataset")
plt.show()