import numpy_p1 as np
import matplotlib.pyplot as plt
days = np.array(["Monday" , "Tuesday" , "wednesday" , "Thursday"])
temperature = np.array([31,32,33,34])
plt.subplot(1,2,1)
plt.plot(days , temperature)

days = np.array(["Friday","Saturday" , "Sunday"])
temperature = np.array([35,3 , 39])

plt.subplot(1,2,2)
plt.plot(days , temperature)

plt.show()