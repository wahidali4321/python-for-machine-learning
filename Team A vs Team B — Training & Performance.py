import numpy as np
import matplotlib.pyplot as plt
study_A = [1, 2, 3, 4, 5, 6]
marks_A = [45, 52, 60, 68, 75, 82]
plt.scatter(study_A , marks_A , marker= '*' , label = "Study A")

study_B = [1, 2, 3, 4, 5, 6]
marks_B = [50, 58, 65, 72, 80, 88]
plt.scatter(study_B , marks_B , marker= '*' , label = "Study B")
plt.title("Team A vs Team B __ Training & Performance")
plt.xlabel("study")
plt.ylabel("marks")
plt.legend()
plt.grid()
plt.show()