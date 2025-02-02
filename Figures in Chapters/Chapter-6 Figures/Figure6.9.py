#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:35:08 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([2,4,5,6,8,11])

y= np.array([18,12,10,8,7,5])

xBar = np.average(x)

yBar=np.average(y)

b0=18.042

b1=-1.340

yPredicted = b0+b1*x

s=2.013 

se_i = s*(1/len(x)+(x-xBar)**2/np.sum((x-xBar)**2))**0.5

t = 2.78

error = t*se_i

plt.figure(1,dpi=600)
plt.scatter(x,y,label='Experiment',s=50,color='r')
plt.errorbar(x, yPredicted, yerr=error, fmt='o', capsize=5,ecolor='green',color='green',label='Predicted')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 
plt.xlabel('X',fontsize=14)
plt.ylabel('Y',fontsize=14)
plt.legend(fontsize=14)
plt.savefig('Figure6.9.png',bbox_inches='tight')
plt.show()