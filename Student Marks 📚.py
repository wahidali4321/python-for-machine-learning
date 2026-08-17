import numpy_p1 as np
import matplotlib.pyplot as plt
Subjects = np.array(['Math', 'Physics', 'English', 'CS', 'Statistics'])
marks = np.array([75, 82, 68, 90, 78])
plt.plot(Subjects , marks , marker = 'o')
plt.title("Student Marks 📚")
plt.xlabel("Subjects")
plt.ylabel("marks")
plt.grid(True)