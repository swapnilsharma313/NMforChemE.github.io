#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:45:50 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

y0=1
solution=[y0]
for i in range(0,4):
    solution.append(-1/5*solution[i])
    
time_step=np.arange(0,5,1)

plt.figure(1,dpi=600)
plt.plot(time_step,solution,linestyle=':',color='black')
plt.scatter(time_step,solution,color='red',marker='s')
plt.grid()
plt.xticks([0,1,2,3,4],fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Number of time steps (n)',fontsize=14)
plt.ylabel(r'$y_n$',fontsize=14)
plt.savefig('Figure4.6.png',bbox_inches='tight')
plt.show()
