# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

l0=lambda a: (a-1)*(a-2)/((0-1)*(0-2))

l1=lambda a: a*(a-2)/((1-0)*(1-2))

l2=lambda a: a*(a-1)/((2-0)*(2-1))

x=np.linspace(0,2,4000)
#%%
plt.figure(1,dpi=600)
plt.plot(x,l0(x),color='black')
plt.plot(x,l1(x),color='red')
plt.plot(x,l2(x),color='green')
plt.legend(['L0','L1','L2'],loc='upper right')
plt.xlim([0,2])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('Figure2.2_NodePolynomial.png')
plt.show()
