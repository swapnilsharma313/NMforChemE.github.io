# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:09:28 2024

@author: ssharm37
"""

#In the linear stability analysis of Lapwood convection problem,
# we come across the following two-point boundary value problem.
# We want to solve the system of equations for differen values of the wavenumber
# and ultimately generate a plot between Rayleigh number and wavenumber.
# We read the minimum of the graph which tells us the critical rayleigh number necessary
# for the onset of natural convection in the Lapwood problem.

#The equations are:
    #f''=w^2.f+w.g and g''=w^2.g+Ra.w.f, where Ra is the Rayleigh number and w is the wavenumber
    #The boundary conditions are f=g=0 at z=0 and 1. 
    #As we can see, we always have the trivial solution satisfying the equations. 
    #This is an eigenvalue problem and we are interested in finding the non-trivial solution. 
    #Therefore, while computing, we will fix the slope of one of the variables at one boundary.
    
########################################################
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

L=1.0 #z coordinate goes from 0 to L
#empty lists to store the solutions
Ra_store=[]
g_prime=[]

#list of wavenumbers we want to compute the solution at
kwave= np.asarray(np.linspace(3.14,7,int(100)).tolist()+np.linspace(3.14,1.0,50).tolist(),dtype='float64')

for i in range(0,len(kwave)):
    w=kwave[i]
    
    #declare the BVP in form of an IVP for shooting method
    def func(t,y):
          
        Eq= np.zeros(y.shape, dtype='float64')
        
        f,f_p,g,g_p,Ra=y
        
        Ra= y[4]
                 
        Eq[0] = f_p
        
        Eq[1] = w**2.0*f+g*w
          
        Eq[2]=g_p
        
        Eq[3]= w**2.0*g+Ra*w*f
        
        Eq[4] = 0
        
        return Eq
      
    #write a function that will solve to satisfy the boundary conditions
    #x will take g_p as x[0] and Ra as x[1]
    def mysolver(x):
           
        IVP = solve_ivp(func,[0,L],[0.0,1.0e-2,0.0,x[0],x[1]],method='LSODA',atol=1e-15,rtol=1e-5)
        #f and g at the boundary
        f_zL,g_zL= IVP.y[0,-1],IVP.y[2,-1]
          
        return [f_zL,g_zL] #boundary condition at z=L,i.e. f=g=0 at z=L
      
    if i==0 or i==100:
        #initialize the solution
        sol = fsolve(mysolver,[1e-3,39.2],xtol=1e-5, epsfcn=1e-8)
        #epsfcn specifies the step size for calculating the jacobian and xtol specifies the solution accuracy
        Ra_store.append(sol[1])
        g_prime.append(sol[0])
        
    else:
        #we will use the previous points as the guess for the next solutions
        sol = fsolve(mysolver,[g_prime[i-1],Ra_store[i-1]])
        Ra_store.append(sol[1])
        g_prime.append(sol[0])
        
########################################################
#Analyzing the solution and making the neutral curve
minRaIndex= Ra_store.index(np.min(Ra_store))

w=kwave[minRaIndex]

print('Minimum Rayleigh number: %.2f' %Ra_store[minRaIndex])

print('Wave number: %.2f' %w)

plt.figure(1,dpi=600)
plt.scatter(kwave,Ra_store,color='Red',s=4)
plt.xlabel('Wavenumber',fontsize=14)
plt.ylabel('Rayleigh Number',fontsize=14)
plt.title('Neutral stability curve',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(linestyle='--')
plt.ylim([25,60]) #crops the limit of values on y-axis
plt.show()
plt.savefig('Neutral_Stability_curve.jpg',bbox_inches='tight')

#########################################################
#Plotting the eigenfunctions at the minimum of the neutral curve

#store the solution at the following point along the z axis
forceStore = np.linspace(0,L,100)

Eigen=solve_ivp(func,[0,L],[0.0,1.0*0.01,0.0,g_prime[minRaIndex],Ra_store[minRaIndex]],method='LSODA',t_eval=forceStore,atol=1e-15,rtol=1e-5)

#Note that the absolute tolerance for LSODA is extremely low.
# This effectively gives the control to relative tolerance only.
# See python documentation to understand how error is calculated.

plt.figure(2,dpi=600)
plt.plot(Eigen.t,Eigen.y[0],color='black',linewidth=2.0)
plt.title('f',fontsize=14)
plt.xlabel('Z',fontsize=14)
plt.ylabel('Amplitude',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(color='green',linestyle='--')
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))
#Sets the format of the float representation on the y-ticks
plt.show()

plt.figure(3,dpi=600)
plt.plot(Eigen.t,Eigen.y[2],color='black',linewidth=2.0)
plt.title('g',fontsize=14)
plt.xlabel('Z',fontsize=14)
plt.ylabel('Amplitude',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(color='green',linestyle='--')
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))
plt.show()
