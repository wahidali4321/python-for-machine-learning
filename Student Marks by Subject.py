import matplotlib.pyplot as plt
import numpy_p1 as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
zpoints = np.array([3, 15])
npoints = np.array([3, 20])

plt.plot(xpoints, ypoints,zpoints, npoints , marker='s')
plt.show()