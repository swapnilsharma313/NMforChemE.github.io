#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:56:08 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

omega= np.array([0,0.25,0.5,0.75,1.0,1.0717,1.25,1.5,1.75,2.0])

lam1= (omega**2-8*omega+8)/8 + np.emath.sqrt((omega**2-8*omega+8)**2/64-(1-omega)**2)
lam2 = (omega**2-8*omega+8)/8 - np.emath.sqrt((omega**2-8*omega+8)**2/64-(1-omega)**2)
#%%

plt.figure(1,dpi=600)
plt.scatter(lam1.real,lam1.imag,color='red')
plt.scatter(lam2.real,lam2.imag,color='black')
plt.xlabel('Real',fontsize=14)
plt.ylabel('Imaginary',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend([r'$\lambda_1$',r'$\lambda_2$'],fontsize=14)
plt.grid()
plt.annotate(r'$\omega$=0, $\lambda_1=\lambda_2=1$',(lam1.real[0],lam1.imag[0]),textcoords="offset points", xytext=(-50,10), ha='center',fontsize=14)

plt.annotate(r'$\omega$=2',(lam1.real[-1],lam1.imag[-1]),textcoords="offset points", xytext=(30,0), ha='center',fontsize=14)

plt.annotate(r'$\omega$=1, $\lambda_1=0.25$, $\lambda_2=0$',(lam1.real[4],lam1.imag[4]),textcoords="offset points", xytext=(-100,-20), ha='center',fontsize=14)

plt.savefig('Figure5.1.png',bbox_inches='tight')
plt.show()
