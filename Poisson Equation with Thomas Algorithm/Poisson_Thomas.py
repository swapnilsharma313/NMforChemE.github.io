#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:27:09 2024

@author: swapnilsharma
"""

import numpy as np
from numpy.linalg import inv
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix #compressed sparse matrix

N=52#number of nodes in x and y including the boundaries. 

#x and y are normalized to go from 0 to 1 each.

#forcing function
def forcing(x,y):
    return 0
#boundary conditions
def boundary_top(x,y):
    return -np.exp(np.pi*x)

def boundary_bottom(x,y):
    return np.exp(np.pi*x)

def boundary_left(x,y):
    return np.cos(np.pi*y)

def boundary_right(x,y):
    return np.exp(np.pi)*np.cos(np.pi*y)

#%%
h=1.0/(N-1.0) #step size

x=y=np.arange(0,1+h,h) #x and y coordinates of the grid points
y=y[::-1].copy()
grid=np.zeros((N,N)) #visual represenation of the grid

#evaluating forcing function at all the grid points. Origin is on bottom-left
forcing_val=np.zeros((N-2,N-2))
for i in range (0,N-2):
    for j in range (0,N-2):
        forcing_val[i,j]=forcing(x[j+1],y[i+1])

grid=np.zeros((N,N))
grid[1:N-1,1:N-1]=forcing_val.copy()  
grid[0,1:N-1]=boundary_top(x[1:N-1],y[0])
grid[1:N-1,0]=boundary_left(x[0],y[1:N-1])
grid[-1,1:N-1]=boundary_bottom(x[1:N-1],y[-1])
grid[1:N-1,-1]=boundary_right(x[-1],y[1:N-1])

#adding boundary values to the neighbouring elements
grid[1,1:N-1]=grid[1,1:N-1]-grid[0,1:N-1]/h**2.0 #top
grid[-2,1:N-1]=grid[-2,1:N-1]-grid[-1,1:N-1]/h**2.0#bottom
grid[1:N-1,1]=grid[1:N-1,1]-grid[1:N-1,0]/h**2.0 #left
grid[1:N-1,-2]=grid[1:N-1,-2]-grid[1:N-1,-1]/h**2.0#right


#%%        

b=-h**2.0*(grid[1:N-1,1:N-1])

#%%
#Method-1 for making the coefficient matrix
D=np.diag(-1.0*np.ones(N-3),-1)+np.diag(4.0*np.ones(N-2),0)+np.diag(-1.0*np.ones(N-3),1)
        
I=-np.identity(N-2)

super_matrix = np.zeros((N-2,N-2,N-2,N-2))

for i in range(0,N-2):
    super_matrix[i,i]=D
    
for i in range(0,N-3):
    super_matrix[i,i+1]=I
    super_matrix[i+1,i]=I
    
#%%    
#Method-2 for making the coefficient matrix
#The coefficient matrix of the Laplacian operator can be represented using kronecker product

def create_poisson_matrix(nx, ny):

    # Create 1D finite difference matrices

    Dxx = np.diag(np.ones(nx)*2, 0) - np.diag(np.ones(nx-1), 1) - np.diag(np.ones(nx-1), -1)

    Dyy = np.diag(np.ones(ny)*2, 0) - np.diag(np.ones(ny-1), 1) - np.diag(np.ones(ny-1), -1)

    # Create identity matrices

    Ix = np.eye(nx)

    Iy = np.eye(ny)

    # Construct the 2D Poisson matrix using Kronecker product

    A = np.kron(Iy, Dxx) + np.kron(Dyy, Ix)

    return A

def split(array, nrows, ncols): #reference: https://stackoverflow.com/questions/11105375/how-to-split-a-matrix-into-4-blocks-using-numpy

    r, h = array.shape
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))

Coeff_Matrix = create_poisson_matrix(N-2,N-2)
super_matrix_kron=split(Coeff_Matrix,N-2,N-2).reshape((N-2,N-2,N-2,N-2))
    
#%%
def thomas(matrix,vector,num):
    A=matrix
    n=num-2
    #forward sweep
    c=np.zeros((n-1,n,n))
    d=vector.copy() #deep copy to avoid changing the original vector
    d_dash=np.zeros((n,n)) #for storing new coefficients
    c[0]=inv(A[0,0])@A[0,1] 
    for i in range(1,n-1):
        c[i]=inv(A[i,i]-A[i,i-1]@c[i-1])@A[i,i+1] 
    d_dash[0]= inv(A[0,0])@d[0] 
    for i in range(1,n):
        d_dash[i]=inv(A[i,i]-A[i,i-1]@c[i-1])@(d[i]-A[i,i-1]@d_dash[i-1]) 
        
    #solution vector
    x=np.zeros((n,n))
    x[-1]=d_dash[-1]
    for i in range (2,n+1):
        x[-i]=d_dash[-i]-c[-i+1]@x[-i+1]
    return x

solution=thomas(super_matrix,b,N)

solution_kron = thomas(super_matrix_kron,b,N)

direct_solution = spsolve(csr_matrix(Coeff_Matrix),b.reshape((N-2)*(N-2)))
#%%
#analytical solution
def analytic(x,y):
    return np.exp(np.pi*x)*np.cos(np.pi*y)

trueSolution=np.zeros((N-2,N-2))
for i in range (0,N-2):
    for j in range (0,N-2):
        trueSolution[i,j]=analytic(x[j+1],y[i+1])

#%%
       
import matplotlib.pyplot as plt

plt.figure(1,dpi=600)
plt.imshow(solution,cmap='rainbow')
plt.title('Thomas Method')
plt.colorbar() 
plt.show()

plt.figure(2,dpi=600)
plt.imshow(trueSolution,cmap='rainbow')
plt.title('Analytical Solution')
plt.colorbar() 
plt.show()

plt.figure(3,dpi=600)
plt.imshow(solution_kron,cmap='rainbow')
plt.title('Thomas Method: Coefficient Matrix using Kronecker Product')
plt.colorbar() 
plt.show()

plt.figure(4,dpi=600)
plt.imshow(direct_solution.reshape((N-2,N-2)),cmap='rainbow')
plt.title('Direct Solution using Sparse Matrix solver')
plt.colorbar() 
plt.show()


#%%
print("Max Error:", np.max(abs(solution-trueSolution)))

#You can now also compare the time taken by different strategies as the grid size increases 
