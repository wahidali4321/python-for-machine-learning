import numpy_p1 as np
import matplotlib.pyplot as plt
sleep_A = [5, 6, 7, 8, 9, 10]
productivity_A = [50, 60, 68, 75, 82, 85]
plt.scatter(sleep_A , productivity_A , marker= 's' , label = "Group A" , color = "black")

sleep_B = [5, 6, 7, 8, 9, 10]
productivity_B = [45, 55, 65, 72, 78, 82]
plt.scatter(sleep_B , productivity_B , marker= 's' , label = "Group B" , color = "green")
plt.title("Group A vs Group B — Sleep & Productivity")
plt.xlabel("Sleep")
plt.ylabel("productivity")
plt.grid(True)
plt.legend()
plt.show()