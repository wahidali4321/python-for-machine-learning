import numpy as np
marks = [11,22,33,44,55,66,77,88,99,12,13,14,15,16,17,18,19,20,21]
tenth = np.percentile(marks , 10)
twentyFive = np.percentile(marks , 25)
fifty = np.percentile(marks , 50)
seventyFive = np.percentile(marks , 75)
ninty = np.percentile(marks , 90)
print("the tenth is : " , tenth)
print("\n the twenty five is : " , twentyFive)
print("\n  the fifty is :  " , fifty )
print("\n the seventy five is : " , seventyFive)
print("\n the ninty is : " , ninty)