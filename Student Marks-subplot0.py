import numpy as np
import matplotlib.pyplot as plt
Subjects = np.array(["Maths" , "Physics" , "English" , "CS"])
Marks = np.array([75, 82, 68, 90])
plt.subplot(1,2,1)
plt.plot(Subjects , Marks)
plt.title("Student Marks")
plt.xlabel('Subjects')
plt.ylabel("Marks")

Subjects = np.array(["Statistics", "AI", "Database", "Web"])
Marks = np.array([78, 85, 88, 92])

plt.subplot(1,2,1)
plt.plot(Subjects , Marks)


plt.show()