#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:01:14 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as patches


fig, ax = plt.subplots()
polygon = Polygon([(0, 0.25), (0, 0.5), (0.5, 0.5),(0.5,0),(0.25,0),(0.25,0.25)], 
                  edgecolor='red', facecolor='lightgray',linewidth=5)
ax.add_patch(polygon)
plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False) 
plt.xlim([0,0.6])
plt.ylim([0,0.6])
plt.text(0.35, 0.35, r'$\Omega$',fontsize=16)
arrow = patches.FancyArrowPatch(
    (0.125,0.125),
    (0.25,0.25),
    mutation_scale=20,  
    arrowstyle='->',  
    connectionstyle='arc3,rad=0.2', 
    color='black'
)
ax.add_patch(arrow)
plt.text(0.08, 0.09, r'$\partial\Omega$',fontsize=16,color='red')
plt.savefig('Figure6.5.png',bbox_inches='tight')
plt.show()