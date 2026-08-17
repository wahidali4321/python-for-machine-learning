import numpy_p1 as np
import matplotlib.pyplot as plt
subjects = np.array(["Math", "Physics", "Chemistry", "English"])
scores = np.array([88, 76, 91, 84])
plt.plot(subjects , scores , 's')
plt.title("Exam scores")
plt.xlabel("subject")
plt.ylabel("scores")
plt.show()