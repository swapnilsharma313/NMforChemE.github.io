#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 06:16:31 2024

@author: swapnilsharma
"""
import matplotlib.pyplot as plt
import numpy as np

# Define the domain
x_start, x_end = 0, 1
y_start, y_end = 0, 1

# Number of grid points in each direction
nx = 10
ny = 10

# Create the grid
x = np.linspace(x_start, x_end, nx)
y = np.linspace(y_start, y_end, ny)
X, Y = np.meshgrid(x, y)

# Plot the mesh
plt.figure(1,dpi=600)
plt.plot(X, Y, 'k-', lw=1.5)
plt.plot(X.T, Y.T, 'k-', lw=1.5)
plt.scatter(X, Y, color='red', s=40)
plt.xlabel('X',fontsize=14)
plt.ylabel('Y',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Figure5.2.png',bbox_inches='tight')
plt.show()
