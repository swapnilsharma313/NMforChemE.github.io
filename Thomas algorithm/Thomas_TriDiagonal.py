# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:58:28 2024

@author: ssharm37
"""

import numpy as np

#We will solve Ax=b where A is a tri-diagnoal system
#Let's declare matrix A and vector b 
A= np.array([[1,6,0,0,0],
             [7,2,8,0,0],
             [0,9,3,10,0],
             [0,0,11,4,12],
             [0,0,0,13,5]])

b=np.array([14,25,17,-1,9])

def thomas(matrix,vector):
    n=matrix.shape[0]
    #forward sweep
    c=np.zeros(n-1)
    d=vector.copy() #deep copy to avoid changing the original vector
    d_dash=np.zeros(n) #for storing new coefficients
    c[0]=matrix[0,1]/A[0,0]
    for i in range(1,n-1):
        c[i]=A[i,i+1]/(A[i,i]-A[i,i-1]*c[i-1])
    d_dash[0]=d[0]/A[0,0]
    for i in range(1,n):
        d_dash[i]=(d[i]-A[i,i-1]*d_dash[i-1])/(A[i,i]-A[i,i-1]*c[i-1])
        
    #solution vector
    x=np.zeros(n)
    x[-1]=d_dash[-1]
    for i in range (2,n+1):
        x[-i]=d_dash[-i]-c[-i+1]*x[-i+1]
    return x

answer=thomas(A,b)

print('Thomas Algorithm answer:', answer)

print('In-built code:',np.linalg.solve(A,b))
        
        
    