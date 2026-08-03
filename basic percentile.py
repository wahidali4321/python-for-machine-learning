import numpy as np
marks = [55, 60, 65, 70, 75, 80, 85, 90]
TF = np.percentile(marks)
ST = np.percentile(marks)
TFS = np.percentile(marks)
print("25% : " , TF)
print("\n 50% : " , ST)
print("\n 75% : " , TFS)