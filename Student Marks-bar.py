import numpy_p1 as np
import matplotlib.pyplot as plt
Subjects = np.array(['Math', 'Physics', 'English', 'CS', 'Statistics'])
Marks = np.array([120, 150, 180, 140, 200])
plt.bar(Subjects , Marks)
plt.title("Monthly Sales")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()