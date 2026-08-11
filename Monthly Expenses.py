import numpy as np
import matplotlib.pyplot as plt
Food = np.array([25])
Transport = np.array([15])
Education = np.array([30])
Shopping = np.array([20])
Other = np.array([10])

values = np.array([Food , Transport , Education , Shopping , Other])
label  = np.array(["Food" , "Transport" , "Eduction" , "shopping" , "other"])
plt.pie(values , label= label)
plt.show()