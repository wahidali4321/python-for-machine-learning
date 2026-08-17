import numpy_p1 as np
import matplotlib.pyplot as plt

subjects = np.array(["Math", "Physics", "Chemistry", "English"])
marks = np.array([75, 82, 90, 88])

plt.plot(
    subjects,
    marks,
    marker='D',      # Diamond marker
    mfc='cyan',      # Marker face color
    mec='blue',      # Marker edge color
    ms=10,           # Marker size
    color='black',   # Line color
    linewidth=3      # Line width
)

plt.title("Student Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)

plt.show()