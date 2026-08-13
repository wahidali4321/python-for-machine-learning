import numpy as np
students = np.array([
    "Ali", "Ahmed", "Usman", "Hamza",
    "Bilal", "Hassan", "Zain", "Omar"
])
print(students[0:3])
print(students[2:6])
print(students[7:4:-1])
print(students[0:7:2])
print(students[7:0:-1])