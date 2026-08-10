import numpy as np
import matplotlib.pyplot as plt
Employees = np.array(['Ali', 'Ahmed', 'Sara', 'John', 'Maria'])
Salaries = np.array([50000, 60000, 55000, 70000, 65000])
plt.bar(Employees , Salaries)
plt.title("Employee Salaries")
plt.xlabel("Employees")
plt.ylabel("Salaries")
plt.show()