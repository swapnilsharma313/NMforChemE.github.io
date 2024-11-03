#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:15:52 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,100)

exact=np.exp(-x)

a=1-1/2**0.5

RosenBrock_2nd_order= (1+x*(2*a-1))/(1+a*x)**2

plt.figure(1,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,RosenBrock_2nd_order,color='red')
plt.legend(['Exact','Rosenbrock 2nd Order'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_a.png')
plt.show()

a=1+1/2**0.5

Modified_RosenBrock= (1+x*(2*a-1))/(1+a*x)**2

plt.figure(2,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,Modified_RosenBrock,color='red')
plt.legend(['Exact','Modified Rosenbrock'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_b.png')
plt.show()

a=0.5

Villadsen_2nd_order = (1+(2*a-1)*x+x*x*(a**2-2*a+0.5))/(1+a*x)**2

plt.figure(3,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,Villadsen_2nd_order,color='red')
plt.legend(['Exact','Villadsen 2nd Order (A-stable)'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_c.png')
plt.show()

a=0.25
x=np.linspace(0,10,100)
Modified_Villadsen = (1+(2*a-1)*x+x*x*(a**2-2*a+0.5))/(1+a*x)**2

plt.figure(4,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,Modified_Villadsen,color='red')
plt.legend(['Exact','Modified Villadsen (A-stable)'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_d.png')
plt.show()

#roots of equation:  A^3-3A^2+1.5A-1/6=0
A=[0.1589839,0.4358665,2.4051495]

def Michelsen(i,x):
    b=A[i]
    return ((3*b**2-3*b+0.5)*x**2+x*(3*b-1)+1)/(1+b*x)**3 
    
plt.figure(5,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,Michelsen(0,x),color='red')
plt.plot(x,Michelsen(1,x),color='green')
plt.plot(x,Michelsen(2,x),color='pink')
plt.legend(['Exact','a=0.1589839','a=0.4358665','a=2.4051495'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_e.png')
plt.show()

plt.figure(6,dpi=600)
plt.plot(x,exact,color='black')
plt.plot(x,1/(1+x),color='red',linestyle=':')
plt.plot(x,1/(1+x+0.5*x**2),color='green',linestyle='--')
plt.plot(x,1/(1+x+0.5*x**2+1/6*x**3),color='pink')
plt.legend(['Exact','Implicit Euler','2nd Order','3rd Order'],fontsize=14)
plt.ylabel('r(x)',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure4.7_f.png')
plt.show()