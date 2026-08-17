import numpy_p1 as np
import matplotlib.pyplot as plt
hours_A = [30, 35, 40, 45, 50, 55]
salary_A = [30, 35, 42, 50, 58, 65]
plt.scatter(hours_A , salary_A , marker= 's' , label = "Department A")

hours_B = [30, 35, 40, 45, 50, 55]
salary_B = [32, 38, 45, 53, 62, 70]
plt.scatter(hours_B , salary_B , marker= 's' , label = "Department B")
plt.title("Department A vs Department B — Working Hours & Salary")
plt.xlabel("hours")
plt.ylabel("salaries")
plt.grid()
plt.legend()
plt.show()