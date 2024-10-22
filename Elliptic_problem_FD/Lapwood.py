# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:46:18 2024

@author: ssharm37
"""

#We are solving the steady state lapwood convection problem.

# We are using pseudo-transient method to solve this elliptic equation.   

import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matplotlib as ml
import scipy.linalg


grid=30 #number of grid points including the boundary


size=grid-1 #a variable to help with indexing the arrays
variable=grid-2 #number of total variables to solve is "variable^2"
x1=np.linspace(0,1,grid) #coordinate of the nodes including the boundary
spacing=x1[1:grid]-x1[0:size] #spacing between nodes

boundaryTheta=np.zeros(grid-2) #boundary conditions for temperature

boundaryPsi=np.zeros(grid-2) #boundary conditions for streamfunction

Ra=65.0 #define the Rayleigh number for which the solution is sought

#Define the equations in the following function.
#We will use second order accurate discretization
#The equations to be solved are :
    #Laplace(Psi)-Ra*dTdx and LaplaceT+dPsidy*dTdx+dPsidx*(1.0-dTdy)
def equations(y):
    #Define the array for storing the equations to be solved
    MomEq=np.zeros((grid,grid))
    EnergyEq=np.zeros((grid,grid))
    
    #define the grid xPsi for streamfunction on the grid that includes BC
    xPsi=np.zeros((grid,grid))
    
    #storing the value of streamfunction at the nodes being solved in tempPsi
    tempPsi=y[0:variable*variable].reshape((grid-2,grid-2))
    
    #enforcing the BC for Psi
    xPsi[0,1:size]=boundaryPsi #Top
    xPsi[size,1:size]=boundaryPsi #Bottom
    xPsi[1:size,0]=boundaryPsi #Left
    xPsi[1:size,size]=boundaryPsi #Right
    xPsi[1:size,1:size]=tempPsi
    
    #define the grid xTheta for temperature on the grid that includes BC
    xTheta=np.zeros((grid,grid))
    
    #storing the value of temperature at the nodes being solved in tempTheta
    tempTheta=y[variable*variable:2*variable*variable].reshape((grid-2,grid-2))
    
    #enforcing the BC for temperature or theta
    xTheta[0,1:size]=boundaryTheta#Top
    xTheta[size,1:size]=boundaryTheta#Bottom
    
    #We will use one sided derivatives for left and right flux type boundary
    xTheta[1:size,0]=(4.0*tempTheta[:,0]-tempTheta[:,1])/3.0#Left
    xTheta[1:size,size]=(4.0*tempTheta[:,-1]-tempTheta[:,-2])/3.0#Right
    xTheta[1:size,1:size]=tempTheta


    #defining the spatial derivatives like dT_dx, dPsi_dy etc.
    dtdx=spacing[0:size-1]**-1.0*(xTheta[1:size,1:size]-xTheta[1:size,0:size-1])
    
    dPsidx=spacing[0:size-1]**-1.0*(xPsi[1:size,1:size]-xPsi[1:size,0:size-1])
    
    #notice for the y-derivatives that we have to use the transpose operation. This is because of the way python multiplies a vector and a matrix
    dtdy=spacing[0:size-1]**-1.0*np.transpose((xTheta[2:grid,1:size]-xTheta[0:size-1,1:size]))*0.5
    
    dtdy=-np.transpose(dtdy) #minus sign is because of the way we define grid
    
    dPsidy=spacing[0:size-1]**-1.0*np.transpose((xPsi[2:grid,1:size]-xPsi[0:size-1,1:size]))*0.5
    
    dPsidy=-np.transpose(dPsidy)
    
    
    LaplaceT=spacing[0:size-1]**-2.0*(-xTheta[1:size,1:size]+xTheta[1:size,0:size-1])+spacing[1:size]**-2.0*(xTheta[1:size,2:grid]-xTheta[1:size,1:size])+(spacing[0:size-1]**-2.0*(xTheta[0:size-1,1:size]-xTheta[1:size,1:size]).T).T+(spacing[1:size]**-2.0*(xTheta[2:grid,1:size]-xTheta[1:size,1:size]).T).T

    LaplacePsi=spacing[0:size-1]**-2.0*(-xPsi[1:size,1:size]+xPsi[1:size,0:size-1])+spacing[1:size]**-2.0*(xPsi[1:size,2:grid]-xPsi[1:size,1:size])+spacing[0:size-1]**-2.0*(xPsi[0:size-1,1:size]-xPsi[1:size,1:size])+spacing[1:size]**-2.0*(xPsi[2:grid,1:size]-xPsi[1:size,1:size])
    
    
    MomEq[1:size,1:size]=LaplacePsi-Ra*dtdx #Momentum Equation
    
   
    EnergyEq[1:size,1:size]=LaplaceT+dPsidy*dtdx+dPsidx*(1.0-dtdy) #Energy Equation
    
    
    Mom=(MomEq[1:size,1:size]).reshape(grid-2*grid-2) #reshape to vector
    E=  (EnergyEq[1:size,1:size]).reshape(grid-2*grid-2)  #reshape to vector
    
    return np.append(Mom,E) #join the vectors to pass to IVP solver


#%%
#Wrapper that enables the use of solve_IVP's syntax and prints progress
def func(t,y):
    print('Time step:',t)
    return equations(y)

guess=random.rand(2*(grid-2)*(grid-2)) #random initialisation.

#initializing using random numbers is not always recommended for more complex problems
# as it can delay the approach to the desired solution. 
#Knowing a prioiri some structure of the solution helps in fast convergence. 
#In case of multiple solutions, a good guess or initial condition becomes even more important.

solution=solve_ivp(func,[0,100],guess,method='BDF')
#%%
sol=solution.y[:,-1] #storing the steady state solution at the final time

error=equations(sol)
error=np.sum(error**2.0)
error=np.sqrt(error)/variable**2.0 #divide by the number of equations
print('Error at final time:',error)

plt.rcParams['font.size'] = 14 #set the fontsize for all plots in one line
plt.figure(1,dpi=600,figsize=(5,5))
x,y=np.meshgrid(x1[1:size],x1[1:size])
plt.contourf(x,y,sol[0:variable**2].reshape((variable,variable)),cmap='rainbow')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Z')
plt.title('Streamlines')
plt.show()

plt.figure(2,dpi=600,figsize=(5,5))
x,y=np.meshgrid(x1[1:size],x1[1:size])
plt.contourf(x,y,sol[variable**2:2*variable**2].reshape((variable,variable)),cmap='rainbow')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Z')
plt.title('Temperature')
plt.show()
