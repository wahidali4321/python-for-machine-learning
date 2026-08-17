import numpy_p1 as np
import matplotlib.pyplot as plt
Days = np.array(["Mon" , 'Tue' , 'wed' , 'thu' , 'fri' , 'sat' , 'sun'])
Expenses = np.array([500, 700, 400, 800, 600, 1000, 900])
plt.bar(Days , Expenses)
plt.title('Weekly Expenses')
plt.xlabel("Day")
plt.ylabel("Expensese")
plt.show()