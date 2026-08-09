import numpy as np
import matplotlib.pyplot as plt
exercise_A = [10, 20, 30, 40, 50, 60]
calories_A = [80, 150, 220, 290, 350, 410]
plt.scatter(exercise_A , calories_A , marker= 's' , label = "Group A" , color = "black")

exercise_B = [10, 20, 30, 40, 50, 60]
calories_B = [90, 165, 235, 305, 375, 450]
plt.scatter(exercise_B , calories_B , marker= 's' , label = "Group B" , color = "green")
plt.title("Group A vs Group B — Exercise & Calories")
plt.xlabel("exercise")
plt.ylabel("calories")
plt.legend()
plt.grid()
plt.show()