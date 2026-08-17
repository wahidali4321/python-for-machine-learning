import numpy_p1 as np
import matplotlib.pyplot as plt
exams = np.array([1, 2, 3, 4, 5])
marks = np.array([65, 72, 80, 78, 90])
plt.plot(exams , marks)
plt.title("Student Performance")
plt.xlabel("Exam Number")
plt.ylabel("Marks")
plt.show()