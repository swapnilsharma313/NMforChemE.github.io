#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:12:39 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt

# Create sample data
x = np.linspace(-5, 0, 100)
y1 = x
y2=abs(x)

# Create the plot
fig, ax = plt.subplots(dpi=600)

plt.figure(1,dpi=600)

# Move the y-axis to the middle
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks([-4,-3,-2,-1,1,2,3,4])
ax.set_yticks([-4,-3,-2,-1,1,2,3,4])
ax.tick_params(axis='both', which='major', labelsize=14)
ax.set_ylim(-5,5)
ax.set_xlim(-5,5)
ax.axvspan(-5,0, color='red', alpha=0.3)
ax.xaxis.set_label_coords(0,0.4)
ax.set_xlabel(r'                  Re($\lambda$) $\rightarrow$',fontsize=14)
ax.set_ylabel(r'                  Im($\lambda$) $\rightarrow$',fontsize=14)
ax.text(-4, 2, 'A-stable', fontsize=14, bbox=dict(facecolor='white', edgecolor='black'))
plt.savefig('Figure4.3.png',bbox_inches='tight')
plt.show()
