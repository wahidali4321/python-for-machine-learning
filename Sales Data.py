import numpy as np
sales = [120, 135, 140, 150, 160, 170, 180, 190, 200]

thirty = np.percentile(sales , 30)
sixty = np.percentile(sales , 60)
ninty = np.percentile(sales , 90)

print("the 30th :  " , thirty)
print("\n the 60th is : " , sixty)
print("\n the 90th is : " , ninty)