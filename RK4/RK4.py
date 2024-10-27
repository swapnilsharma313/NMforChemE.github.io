#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:22:47 2024

@author: swapnilsharma
"""
import numpy as np
import matplotlib.pyplot as plt

def foo(t,y):
    return -y*np.log(y)

def RK4(func,initial_cond,initial_time,final_time,time_step):
    iterations=int((final_time-initial_time)/time_step)
    y=initial_cond
    t=initial_time
    solution=[y]
    time_stamp=[t]
    for i in range (0,iterations):
        a1=func(t,y)
        a2=func(t+time_step/2.0,y+time_step*a1/2.0)
        a3=func(t+time_step/2.0,y+time_step*a2/2.0)
        a4=func(t+time_step,y+time_step*a3)
        y=y+time_step/6.0*(a1+2.0*a2+2.0*a3+a4)
        t=t+time_step
        solution.append(y)
        time_stamp.append(t)
        print('Time:',t)
    return solution,time_stamp

initial_cond=np.array([0.5])
initial_time=0.0
final_time=1.0
time_step=0.25
solution,time_stamp=RK4(foo,initial_cond,initial_time,final_time,time_step)

def analytical(t):
    return np.exp(np.exp(-t)*np.log(0.5))#-np.log(np.log(y)/np.log(0.5))=t

plt.figure(1,dpi=600)
plt.scatter(time_stamp,solution,marker='o',s=40.0,color='red')
plt.plot(time_stamp,analytical(np.array(time_stamp)),color='black')
plt.ylim([0,1])
plt.xlabel('time',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('y',fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Figure4.8.png')
plt.show()