# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:29:58 2023

@author: ssharm37
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, approx_fprime

#writing Broyden's method for non-linear equations

#define equations
def eqn(p):
    x=p[0]
    y=p[1]
    z=p[2]
    f=np.zeros(len(p))
    f[0]= x**2.0+y**2.0+z**2.0-3.0
    f[1]= x**2.0+y**2.0-z-1.0
    f[2]= x+y+z-3.0
    
    return f

#define jacobian for first iteration
def jac(p):
    return approx_fprime(p,eqn,epsilon=1e-8)

#define accuracy
accuracy=1e-4

#define Sherman Morrison formula
def sm(matrix,u,v):
    inverse= np.linalg.inv(matrix)
    factor= np.dot(v,np.dot(inverse,u))
    uvtA1= np.matmul(np.outer(u,v),inverse)
    return inverse-1.0/(1.0+factor)*np.matmul(inverse,uvtA1)


#define Broyden solver
def broyden(guess,iterations):
    #input initial guess
    jack=jac(guess) #compute initial jacobian value
    delta= np.linalg.solve(jack,-eqn(guess)) #solve for first new value of x
    lam=1.0 #reduce this for controlling the change in input vector
    xnew=guess+lam*delta
    
    for i in range(0,iterations):
        qk= eqn(xnew)-eqn(guess)
        pk=xnew-guess
        jack= jack + (qk-np.dot(jack,pk))/np.dot(pk,pk)*pk
        usm=(qk-np.dot(jack,pk))/np.dot(pk,pk)
        jackinv=sm(jack,usm,pk)
        jack= jack + (qk-np.dot(jack,pk))/np.dot(pk,pk)*pk
        guess=xnew
        xnew=xnew-lam*np.dot(jackinv,eqn(xnew))
        error=np.max(np.sqrt(eqn(xnew)**2.0))
        if (error<=accuracy):
            ans=xnew
            print(ans)
            print('Convergence achieved')
            print('error:',error)
            return ans
        if i>iterations-2:
            print('More iterations required')
            print('error:',error)
            ans=xnew
            return ans        
            
#Execute
answer=broyden([1.0,0.0,10.0],300)

#Exercise: Change the tolerane of jacobian calculation and see the effect on number of iterations required.
# Also, study the effect of changing the factor 'lam' inside the 'broyden' function.
                
    

    