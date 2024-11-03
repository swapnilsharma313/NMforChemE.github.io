#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:56:08 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(1e-7,10,int(1e7))

lam=1e6 #machine precision

e=np.exp(1)

y1=0.5*(e**(-t)+e**(-lam*t))

y2=0.5*(e**(-t)-e**(-lam*t))

plt.figure(1,dpi=600)
plt.plot(t,y1,color='red')
plt.plot(t,y2,color='black',linestyle='--')
plt.xscale("log")
plt.xlabel('time',fontsize=14)
plt.ylabel(r'$y_i$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend([r'$y_1$',r'$y_2$'],fontsize=14)
plt.savefig('Figure4.1.png',bbox_inches='tight')
plt.show()
