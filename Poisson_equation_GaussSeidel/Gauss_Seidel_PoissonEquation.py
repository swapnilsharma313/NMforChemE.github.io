# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:57:20 2024

@author: ssharm37
"""

import numpy as np

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

b=np.reshape(grid[1:N-1,1:N-1],(N-2*N-2))#converting the grid to a vector for Ax=b


#%%

D=np.diag(-1.0*np.ones(N-3),-1)+np.diag(4.0*np.ones(N-2),0)+np.diag(-1.0*np.ones(N-3),1)
        
I=-np.identity(N-2)

O= np.zeros((N-2,N-2))

num_points=int((N-2)*(N-2))

filler=int((num_points-2*(N-2))/(N-2))

super_matrix=[I]
super_matrix.extend([D])
super_matrix.extend([I])
for i in range(0,filler):
    super_matrix.extend([O])

super_matrix=np.array(super_matrix)

def CoefficientMatrix(z):
    n=z.shape[1]
    m=z.shape[0]
    F=np.zeros((n*n,n,n))
    M=np.zeros((n*n,n*n))
    for i in range(0,n):
        F[i*n:n+i*n]=np.take(z,range(1-i,m-i),mode='wrap',axis=0)
    for i in range(0,n):
        M[i*n:n+n*i,:]=np.hstack(F[i*n:n+n*i])
    u,l=np.triu(M,1),np.tril(M,-1)
    d=M-u-l
    return u,l,d #return upper part, lower part and diagonal of the matrix
    
def GaussSeidel(z,b,guess,iterations):
    u,l,d=CoefficientMatrix(z)
    #solving Ax=b
    #where A=u+l+d
    x=guess
    c1=np.linalg.inv(d+l)
    b1=c1@(-b*h**2.0)
    c2=-np.matmul(c1,u)
    for i in range (0,iterations):
        for j in range(0,len(x)):
            x[j]=c2[j,:]@x+b1[j] #use the latest updated value
        print("Iteration:",i)
    return x
    

guess=np.random.rand((N-2)*(N-2)) #random guess to initialize the solution
solution=GaussSeidel(super_matrix,b,guess,1000)
solution=solution.reshape((N-2,N-2)) #reshaping the solution to grid for visualization

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
plt.title('Gauss-Seidel Method')
plt.colorbar() 
plt.show()

plt.figure(2,dpi=600)
plt.imshow(trueSolution,cmap='rainbow')
plt.title('Analytical Solution')
plt.colorbar() 
plt.show()

print("Max Error:", np.max(abs(solution-trueSolution)))
