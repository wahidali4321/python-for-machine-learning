import matplotlib.pyplot as plt
import numpy_p1 as np
study_hours_A = [1, 2, 3, 4, 5, 6]
marks_A = [45, 52, 60, 68, 75, 82]
plt.scatter(study_hours_A , marks_A , marker = 'o' , color = "red" , label = "study_hours_A")


study_hours_B = [1, 2, 3, 4, 5, 6]
marks_B = [50, 58, 65, 72, 80, 88]
plt.scatter(study_hours_B , marks_B , marker = 'o' , color = "yellow" , label = "study_hours_B")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.grid()
plt.legend()
plt.show()