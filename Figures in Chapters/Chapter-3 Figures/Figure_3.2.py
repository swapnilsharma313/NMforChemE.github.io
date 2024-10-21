#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:54:41 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

h=np.linspace(1e-8,1,int(1e7))

delta=1e-8 #machine precision

error=delta+h**4

plt.figure(1,dpi=600)
plt.plot(h,error,color='red')
plt.xscale("log")
plt.yscale("log")
plt.xlabel('Step size',fontsize=14)
plt.ylabel(r'$\epsilon_{total}$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.savefig('Figure3.2.png',bbox_inches='tight')
plt.show()
