import numpy_p1 as np
import matplotlib.pyplot as plt
randnms = np.random.uniform(1 , 100 , 100)
his = plt.hist(randnms , 6)
plt.show()