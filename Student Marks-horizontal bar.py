import numpy_p1 as np
import matplotlib.pyplot as plt
Subjects = np.array(["Maths" , "physics" , "English" , "CS" , "Statistics"])
marks = np.array([75, 82, 68, 90, 78])
plt.barh(Subjects , marks)
plt.title("Student Marks")
plt.show()