# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:37:26 2024

@author: ssharm37
"""

import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
from ode import *
from algorithm import *

y=read_csv("Solution.csv",header=None)

y1,y2,y3=y[0],y[1],y[2]

t=read_csv("Time_stamp.csv",header=None)

#solution from in-built function
inbuilt_sol=solve_ivp(foo_inbuilt,[initial_time,final_time],initial_cond,method='LSODA')

#%%

plt.figure(1,dpi=600)
plt.plot(t,y1,color='red',linewidth=2.0)
plt.plot(t,y3,color='green',linestyle='dashed',linewidth=2.0)
plt.plot(inbuilt_sol.t,inbuilt_sol.y[0],color='black',linestyle=':',linewidth=5.0)
plt.plot(inbuilt_sol.t,inbuilt_sol.y[2],color='pink',linestyle=':',linewidth=5.0)
plt.legend(['$Y_{1}$','$Y_{3}$',r'Inbuilt $Y_{1}$',r'Inbuilt $Y_{3}$'],fontsize=16)
plt.xlabel('Time',fontsize=16)
plt.ylabel('Variable',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.title('Integration using SIRK',fontsize=16)
plt.show()

plt.figure(2,dpi=600)
plt.plot(t,y2,color='black',linestyle='dotted',linewidth=2.0)
plt.xlabel('Time',fontsize=16)
plt.ylabel('$Y_{2}$',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.title('Integration using SIRK',fontsize=16)
plt.show()
