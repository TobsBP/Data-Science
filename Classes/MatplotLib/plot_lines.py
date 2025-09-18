import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

z = x * 6
t = z * z

plt.plot(x,y, '*:r', z,t, 'y', linewidth=5, markersize=10)

plt.xlabel("Axis X")
plt.ylabel("Axis Y")

plt.show()