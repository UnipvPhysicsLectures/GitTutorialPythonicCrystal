# import plot libraries
import matplotlib.pyplot as plt
# import numpy linear algebra library
import numpy as np
 
# create figure
fig,ax = plt.subplots()
 
# 1D arrays for x and y coordinates
n_points = 500
x_min,x_max = -5,5
y_min,y_max = -5,5
X = np.linspace(x_min,x_max, n_points)
Y = np.linspace(y_min,y_max, n_points)
 
# 2D X,Y grids from 1D arrays
X, Y = np.meshgrid(X, Y)
 
# Z 2D grid for the plot
R = np.sqrt(X**2 + Y**2)
Z = np.cos(0.75*R)
 
# plot the surface.
surf = ax.imshow(Z, cmap='magma',origin='lower')
 
# Add a color bar
fig.colorbar(surf)
 
# plot
plt.show()
