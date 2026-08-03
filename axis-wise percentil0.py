6

import numpy as np

import numpy as np



scores = np.array([

    [80, 85, 90],

    [70, 75, 80],

    [60, 65, 70]

])



column_axis = np.percentile(scores , 50 , axis= 1)

row_axis = np.percentile(scores ,50 , axis= 0 )



print("the column axis is : " , column_axis)

print("the row axis is : " , row_axis)