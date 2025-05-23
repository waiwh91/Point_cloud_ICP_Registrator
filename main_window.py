import matplotlib.pyplot as plt

import sys
import numpy as np
import open3d as o3d

pcd_load = o3d.io.read_point_cloud('/home/martin/Point-Cloud-Registration/Data/002/1719040752000000.pcd')

pcd_array = np.asarray(pcd_load.points)

x = pcd_array[:, 0]
y = pcd_array[:, 1]
z = pcd_array[:, 2]


fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)
plt.show()