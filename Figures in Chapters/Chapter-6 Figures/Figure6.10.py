#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:36:11 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure(1,dpi=600)
x=np.linspace(0,1,50)
y=(x-0.5)**2
plt.plot(y,x,color='red')
plt.text(0.01, 0.45, r'Bifurcation point',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 
plt.scatter(0,0.5,color='g',s=80)
plt.xlabel(r'$\alpha$',fontsize=14)
plt.ylabel(r'$x_i$',fontsize=14)
plt.savefig('Figure6.10(a).png',bbox_inches='tight')
plt.show()

#%%
plt.figure(2,dpi=600)
x=np.linspace(0.1,1,50)
y=1/x
plt.plot(y,x,color='red')
plt.plot(10*x,x,color='red')
plt.text(4, 0.3, r'Bifurcation point',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 
plt.scatter(3.15,0.315,color='g',s=80)
plt.xlabel(r'$\alpha$',fontsize=14)
plt.ylabel(r'$x_i$',fontsize=14)
plt.savefig('Figure6.10(b).png',bbox_inches='tight')
plt.show()