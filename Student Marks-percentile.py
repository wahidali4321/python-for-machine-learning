import numpy as np
marks = [65, 70, 75, 80, 85, 90, 95]
TF = np.percentile(marks , 25)
FT = np.percentile(marks , 50)
SF = np.percentile(marks , 75)
print("\n Twenty Five : " , TF)
print("\n Fifty : " , FT)
print("\n seventy Five : " , SF)