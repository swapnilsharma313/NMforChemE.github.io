#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:53:20 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

lh=np.linspace(0,1.25,100)

mu1=0.5*((1-1.5*lh)+np.sqrt(1-lh+9/4*lh**2))

mu2=0.5*((1-1.5*lh)-np.sqrt(1-lh+9/4*lh**2))

plt.figure(1,dpi=600)
plt.plot(lh,mu1,color='red')
plt.plot(lh,mu2,color='blue')
plt.grid()
plt.plot(lh,np.ones(100)*(-1),color='black',linestyle=':')
plt.xlabel(r'$\lambda$ h',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend([r'$\mu_1$',r'$\mu_2$'],fontsize=14)
plt.savefig('Figure4.2.png',bbox_inches='tight')
plt.show()