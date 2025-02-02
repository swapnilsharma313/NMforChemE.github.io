#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:58:52 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure(1,dpi=600)
circle=plt.Circle((0,0),1,fill=False,linestyle='--',linewidth=1,edgecolor='r')
fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xticks([-3,-2,-1,1,2,3])
ax.set_yticks([-3,-2,2,3])
ax.tick_params(axis='both', which='major', labelsize=14)
plt.gca().set_aspect('equal', adjustable='box')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

arrow1 = patches.FancyArrowPatch(
    (1.4,1.4),
    (2.8,2.8),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow1)

arrow11 = patches.FancyArrowPatch(
    (0.7,0.7),
    (0.1,0.1),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow11)


arrow2 = patches.FancyArrowPatch(
    (-1.4,-1.4),
    (-2.8,-2.8),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow2)

arrow22 = patches.FancyArrowPatch(
    (-0.7,-0.7),
    (-0.1,-0.1),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow22)

arrow3 = patches.FancyArrowPatch(
    (-1.4,1.4),
    (-2.8,2.8),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow3)

arrow33 = patches.FancyArrowPatch(
    (-0.7,0.7),
    (-0.1,0.1),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow33)

arrow4 = patches.FancyArrowPatch(
    (1.4,-1.4),
    (2.8,-2.8),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow4)

arrow44 = patches.FancyArrowPatch(
    (0.7,-0.7),
    (0.1,-0.1),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='-', 
    color='black'
)
ax.add_patch(arrow44)

plt.scatter(0,0,color='green',s=50)
plt.text(2, -0.8, r'x$\rightarrow$',fontsize=16)
plt.text(0.2, 2, r'y$\rightarrow$',fontsize=16,rotation=90)
plt.savefig('Figure6.2.png',bbox_inches='tight')
plt.show()