#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:23:29 2024

@author: swapnilsharma
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.interpolate import interp1d


x=np.linspace(0,1,11)

x_sample=np.array([0,0.2,0.5,0.6])
y_sample=np.array([0.2,0.4,0.45,0.45])
f = interp1d(x_sample, y_sample, kind='cubic')
x_smooth = np.linspace(x_sample.min(), x_sample.max(), 10)
y_smooth = f(x_smooth)
#%%

plt.figure(1,dpi=600)
fig, ax = plt.subplots()
plt.plot(x,x,color='black',linestyle='--')
plt.plot(x_smooth, y_smooth,linewidth=3,color='red')

arrow1 = patches.FancyArrowPatch(
    (0.1,0.0),
    (0.1,f(0.1)),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow1)

plt.text(0.1+0.01, 0.025, r'$x^{(0)}$',fontsize=16)

plt.text(0.1-0.05, f(0.1)+0.05, r'$\phi(x)$',fontsize=16)

arrow2 = patches.FancyArrowPatch(
    (0.1,f(0.1)),
    (f(0.1),f(0.1)),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow2)

plt.text(f(0.1)+0.01, f(0.1)-0.05, r'$x^{(1)}$',fontsize=16)

arrow3 = patches.FancyArrowPatch(
    (f(0.1),f(0.1)),
    (f(0.1),f(f(0.1))),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow3)

plt.scatter(f(f(0.1)),f(f(0.1)),color='green',s=100)

plt.text(f(f(0.1)), f(f(0.1))-0.07, r'$x^*$',fontsize=16)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 

plt.xlabel(r'$x^{(k)}$',fontsize=16)
plt.ylabel(r'$x^{(k+1)}$',fontsize=16)

plt.savefig('Figure6.1(a).png',bbox_inches='tight')
plt.show()

#%%
plt.figure(2,dpi=600)
fig, ax = plt.subplots()
plt.plot(x,x,color='black',linestyle='--')
plt.plot(x, 1-0.5*x,linewidth=3,color='red')

arrow1 = patches.FancyArrowPatch(
    (0.1,0.0),
    (0.1,1-0.5*0.1),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow1)

plt.text(0.1+0.01, 0.025, r'$x^{(0)}$',fontsize=16)

plt.text(0.2, 0.77, r'$\phi(x)$',fontsize=16)

arrow2 = patches.FancyArrowPatch(
    (0.1,1-0.05),
    (0.95,0.95),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow2)

plt.text(0.85+0.01, 0.8-0.05, r'$x^{(1)}$',fontsize=16)

arrow3 = patches.FancyArrowPatch(
    (0.95,0.95),
    (0.95,1-0.5*0.95),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow3)

arrow4 = patches.FancyArrowPatch(
    (0.95,1-0.5*0.95),
    (1-0.5*0.95,1-0.5*0.95),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow4)

plt.scatter(1/1.5,1/1.5,color='green',s=100)

plt.text(1/1.5, 1/1.5-0.1, r'$x^*$',fontsize=16)


plt.text(0.5, 0.4, r'$x^{(2)}$',fontsize=16)

arrow5 = patches.FancyArrowPatch(
    (0.525,0.525),
    (0.525,1-0.5*0.525),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow5)

arrow6 = patches.FancyArrowPatch(
    (0.525,0.7375),
    (0.7375,0.7375),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow6)

plt.text(0.7375-0.05, 0.7375+0.05, r'$x^{(3)}$',fontsize=16)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 

plt.xlabel(r'$x^{(k)}$',fontsize=16)
plt.ylabel(r'$x^{(k+1)}$',fontsize=16)

plt.savefig('Figure6.1(b).png',bbox_inches='tight')
plt.show()

#%%

plt.figure(3,dpi=600)
fig, ax = plt.subplots()
plt.plot(x,x,color='black',linestyle='--')
plt.plot(x, 3*x-0.2*3,linewidth=3,color='red')

arrow1 = patches.FancyArrowPatch(
    (0.4,0.4),
    (0.4,0.6),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow1)

plt.text(0.4, 0.35, r'$x^{(1)}$',fontsize=16)

plt.text(0.35, 0.8, r'$\phi(x)$',fontsize=16)

arrow2 = patches.FancyArrowPatch(
    (0.4,0.6),
    (0.6,0.6),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow2)

plt.text(0.35, 0.15, r'$x^{(0)}$',fontsize=16)

arrow3 = patches.FancyArrowPatch(
    (0.33,0.4),
    (0.4,0.4),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow3)

plt.scatter(0.3,0.3,color='green',s=100)

plt.text(0.25, 0.3, r'$x^*$',fontsize=16)

arrow4 = patches.FancyArrowPatch(
    (0.33,0),
    (0.33,0.4),
    mutation_scale=20,  
    arrowstyle='->',  linestyle='--', 
    color='black'
)
ax.add_patch(arrow4)

plt.text(0.6, 0.55, r'$x^{(2)}$',fontsize=16)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14) 

plt.xlabel(r'$x^{(k)}$',fontsize=16)
plt.ylabel(r'$x^{(k+1)}$',fontsize=16)

plt.savefig('Figure6.1(c).png',bbox_inches='tight')
plt.show()
