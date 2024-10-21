# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicHermiteSpline
from numpy.polynomial.polynomial import Polynomial

function=lambda x: sin(x)**5+cos(x)**3+1.5**x

derivative= lambda x: 5*sin(x)**4*cos(x)-3*cos(x)**2*sin(x)+1.5**x*np.log(1.5)

z=np.linspace(0,3.14,1000)

z_points=np.array([0,0.75,1.5,2.25,3])

values=function(z_points)

slope=derivative(z_points)

polyL=lagrange(z_points,values)

polyH=CubicHermiteSpline(z_points, values, slope)
#%%
plt.figure(1,dpi=600)
plt.plot(z,function(z),color='black',label='Function',linestyle='dotted')
plt.plot(z,Polynomial(polyL.coef[::-1])(z),color='red',label='Lagrange',linestyle='--')
plt.plot(z,polyH(z),color='green',label='Hermite',linestyle='dashdot')
plt.legend(['Function','Lagrange','Hermite'])
plt.scatter(z_points,values,marker=10,s=60,color='blue')
plt.xlim([0,3.14])
plt.grid()
plt.xlabel('Z',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.text(1.2, 2.0, r'f(x)=$sin^{2}(x)$+$cos^{3}(x)$+$1.5^{x}$', fontsize = 16)
plt.savefig('Figure2.4_LagrangeHermite.png')
plt.show()
