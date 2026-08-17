import numpy_p1 as np
import matplotlib.pyplot as plt

randnms = np.random.uniform(1, 100, 100)

count, bins, patches = plt.hist(randnms, bins=6)

print("Count:", count)
print("Bin edges:", bins)

plt.xlabel("Random Numbers")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers")
plt.show()