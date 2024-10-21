# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:18:38 2024

@author: ssharm37
"""

from ode import foo
import csv
import numpy as np

def RK45(func,initial_cond,initial_time,final_time,time_step,error):
    #Declaring the Fehlberg Table
    A=[0,2/9,1/3,3/4,1,5/6]
    B=[[2/9],[1/12,1/4],[69/128,-243/128,135/64],[-17/12,27/4,-27/5,16/15],[65/432,-5/16,13/16,4/27,5/144]]
    C=[1/9,0,9/20,16/45,1/12]
    CH=[47/450,0,12/25,32/225,1/30,6/25]
    CT=[1/150,0,-3/100,16/75,1/20,-6/25]
    
    y=initial_cond
    t=initial_time
    solution=[y]
    time_stamp=[t]
    h=time_step
    while t<=final_time:
        a1=h*func(t+A[0]*h,y)
        a2=h*func(t+A[1]*h,y+B[0][0]*a1)
        a3=h*func(t+A[2]*h,y+B[1][0]*a1+B[1][1]*a2)
        a4=h*func(t+A[3]*h,y+B[2][0]*a1+B[2][1]*a2+B[2][2]*a3)
        a5=h*func(t+A[4]*h,y+B[3][0]*a1+B[3][1]*a2+B[3][2]*a3+B[3][3]*a4)
        a6=h*func(t+A[5]*h,y+B[4][0]*a1+B[4][1]*a2+B[4][2]*a3+B[4][3]*a4+B[4][4]*a5)
        y_old=y
        y=y_old+CH[0]*a1+CH[1]*a2+CH[2]*a3+CH[3]*a4+CH[4]*a5+CH[5]*a6
        
        TE=np.abs(CT[0]*a1+CT[1]*a2+CT[2]*a3+CT[3]*a4+CT[4]*a5+CT[5]*a6)
        TE=np.max(TE)
        
        if TE>=error:
            t=t
            h_new=0.9*h*(error/TE)**0.2
            h=h_new
            y=y_old
        else:
            h=h
            t=t+h    
            solution.append(y)
            time_stamp.append(t)
        print('Time:',t)
    return solution,time_stamp

initial_cond=np.array([1.0,0.0,0.0])
initial_time=0.0
final_time=50.0
time_step=1e-3
error=1e-4
solution,time_stamp=RK45(foo,initial_cond,initial_time,final_time,time_step,error)
    
np.savetxt('Solution.csv',solution,delimiter=',')
np.savetxt('Time_stamp.csv',time_stamp)