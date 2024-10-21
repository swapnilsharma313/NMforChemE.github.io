# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

l0=lambda z: (1+2*z)*(1-z)**2 
    
l0H=lambda z: z*(1-z)**2

l1=lambda z: (1+2*(1-z))*z**2

l1H=lambda z: -z**2*(1-z)

x=np.linspace(0,1,1000)
#%%
plt.figure(1,dpi=600)
plt.plot(x,l0(x),color='black')
plt.plot(x,l0H(x),color='black',linestyle='--')
plt.plot(x,l1(x),color='green')
plt.plot(x,l1H(x),color='green',linestyle='--')
plt.legend(['L0','L0_hat','L1','L1_hat'],loc='upper right')
plt.xlim([0,1])
plt.grid()
plt.xlabel('Z',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('Figure2.3_HermiteNodePolynomial.png')
plt.show()
