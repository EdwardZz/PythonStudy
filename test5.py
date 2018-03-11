#Program : made for matplotlib test
#History : 2018-3-11   zhuyongjie

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
# X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
#height value
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
ax.contour(X,Y,Z,zdir='x',offset=-4,cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()

