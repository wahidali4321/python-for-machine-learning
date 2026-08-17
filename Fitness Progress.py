import numpy_p1 as np
import matplotlib.pyplot as plt
weeks = np.array([1, 2, 3, 4, 5, 6])
pushups = np.array([15, 18, 20, 24, 27, 30])

plt.plot(weeks , pushups , '^')
plt.title("Fitness progress")
plt.xlabel("weeks")
plt.ylabel("pushups")
plt.show()