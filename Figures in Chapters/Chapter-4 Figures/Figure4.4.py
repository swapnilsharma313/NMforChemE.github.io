#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:44:49 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

lh=np.linspace(0,6,100)

euler=1-lh

back_euler=1/(1+lh)

trapezoidal= (1-lh/2)/(1+lh/2)

RK2=1-lh+lh**2/2

RK4=1-lh+lh**2/2-lh**3/6+lh**4/24

exact=np.exp(-lh)

plt.figure(1,dpi=600)
plt.plot(lh,euler,color='red',linestyle=':')
plt.plot(lh,back_euler,color='blue',linestyle='--')
plt.plot(lh,trapezoidal,color='green',linestyle='-.')
plt.scatter(lh,RK2,color='orange',marker='+',s=4)
plt.scatter(lh,RK4,color='magenta',marker='D',s=4)
plt.plot(lh,exact,color='black')
plt.ylim([-1,1])
plt.grid()
plt.xlabel(r'$\lambda$h',fontsize=14)
plt.ylabel(r'$r_{mn}(\lambda h)$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(['Euler','Backward Euler','Trapezoid','RK2','RK4','Exact'],fontsize=14,bbox_to_anchor=(1.5, 1),loc='upper right')
plt.savefig('Figure4.4.png',bbox_inches='tight')
plt.show()
