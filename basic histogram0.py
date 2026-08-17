import numpy_p1 as np
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

counts, bins, patches = plt.hist(marks, bins=5)

print("Histogram counts:", counts)
print("Bin edges:", bins)

plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()