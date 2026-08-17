import numpy_p1 as np
heights = [150, 155, 160, 162, 165, 168, 170, 172, 175, 180]
Tenth = np.percentile(heights , 10)
Nintyth = np.percentile(heights , 90)
print("\n the tenth :  " , Tenth)
print("\n the ninty : " , Nintyth)