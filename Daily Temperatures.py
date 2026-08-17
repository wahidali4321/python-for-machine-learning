import numpy_p1 as np
temperatures = [30, 32, 31, 35, 34, 36, 33, 37, 38, 39]

Twenth = np.percentile(temperatures , 20)
Fourthy = np.percentile(temperatures , 40)
Eigthy = np.percentile(temperatures , 80)
print("\n the 20th is : " , Twenth)
print("\n the fourthy is : " , Fourthy)
print("\n the eighth is : " , Eigthy)