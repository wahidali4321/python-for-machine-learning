import numpy_p1 as np
import matplotlib.pyplot as plt
Python = 40
JavaScript = 25
C = 20
Java = 15
values = np.array([Python , JavaScript , C , Java])
labels = np.array(["Python " , "Javascript" , "C" , "Java"])
plt.pie(values , labels = labels , autopct="%1.1f%%")
plt.title("Favorite Programming Languages")
plt.show()