import numpy_p1 as np
import matplotlib.pyplot as plt
subjects = ["Math", "Physics", "English", "CS", "Statistics"]
marks = [75, 82, 68, 90, 78]
plt.plot(subjects , marks , marker = 'o')
plt.grid(True)
plt.title("Student Marks")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()