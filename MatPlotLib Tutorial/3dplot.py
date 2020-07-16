import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,3,5,7,9,1,3]
z = np.ones(10)

#ax.scatter(x, y, z)

dx = np.ones(10)
dy = np.ones(10)
dz = [2,3,4,5,6,7,8,9,1,0]

ax.bar3d(x, y, z, dx, dy, dz)



ax.set_title("3D Plot")
ax.set_xlabel("X axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()