import numpy as np
import matplotlib.pyplot as plt
subjects = ["Math", "Physics", "Chemistry", "English", "Biology"]
marks = [78, 85, 90, 82, 88]
plt.plot(subjects , marks , marker = 'o' , mec = 'r')
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("Student Marks")