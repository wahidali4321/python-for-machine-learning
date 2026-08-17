import numpy_p1 as np
import matplotlib.pyplot as plt
temperature_A = [20, 22, 25, 28, 30, 32]
usage_A = [120, 135, 150, 175, 190, 210]
plt.scatter(temperature_A , usage_A , marker= '*' , color = "Green" , label = "City A")

temperature_B = [20, 22, 25, 28, 30, 32]
usage_B = [100, 115, 140, 160, 180, 195]
plt.scatter(temperature_B , usage_B , marker= '*' , color = "Blue" , label = "City  B")
plt.grid(True)
plt.xlabel("Temperature")
plt.ylabel("Useage")
plt.legend()
plt.title("City A vs City B — Temperature & Electricity Usage")
plt.show()
