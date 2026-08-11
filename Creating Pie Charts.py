import numpy as np
import matplotlib.pyplot as plt
Study = np.array([40])
Sleep = np.array([30])
Exercise = np.array([10])
Entertainment = np.array([20])
plt.title("Creating Pie Charts")
plt.pie(Study , Sleep , Exercise , Entertainment)
plt.show()