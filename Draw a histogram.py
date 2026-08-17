import numpy_p1
import matplotlib.pyplot as plt

x = numpy_p1.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()