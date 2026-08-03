import numpy as np
marks = [55, 60, 65, 70, 75, 80, 85, 90]
TF = np.percentile(marks , 25)
ST = np.percentile(marks , 50)
TFS = np.percentile(marks , 75)
print("25% : " , TF)
print("\n 50% : " , ST)
print("\n 75% : " , TFS)