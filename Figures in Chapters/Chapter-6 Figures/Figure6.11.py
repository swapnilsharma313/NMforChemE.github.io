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
circle=plt.Circle((0.5,0.5),0.25,fill=False)
fig, ax = plt.subplots()
ax.add_patch(circle)
plt.text(0.5, 0.55, r'$\vec{x}^*$',fontsize=16)

plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False) 
square = patches.Rectangle((0.55, 0.5), 0.025, 0.025, linewidth=1, edgecolor='r', facecolor='r')
ax.add_patch(square)
square1 = patches.Rectangle((0.35, 0.6), 0.025, 0.025, linewidth=1, edgecolor='r', facecolor='r')
ax.add_patch(square1)
plt.text(0.4, 0.65, r'$\vec{a}$',fontsize=16)
arrow = patches.FancyArrowPatch(
    (0.36,0.6),
    (0.55,0.5),
    mutation_scale=20,  
    arrowstyle='->',  
    connectionstyle='arc3,rad=0.2', 
    color='black'
)
ax.add_patch(arrow)
plt.text(0.5, 0.8, r'Homotopy in $\mathbb{R}^2$',fontsize=16)
plt.savefig('Figure6.11.png',bbox_inches='tight')
plt.show()