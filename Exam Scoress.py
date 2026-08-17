import numpy_p1 as np
import matplotlib.pyplot as plt
students = np.array([1,2,3,4,5,6])
scores = np.array([55, 68, 75, 82, 90, 95])
plt.title("Exam Scores")
plt.xlabel("student")
plt.ylabel("scores")
plt.plot(students , scores)
plt.show()