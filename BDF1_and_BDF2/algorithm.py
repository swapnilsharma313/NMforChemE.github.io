# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:18:38 2024

@author: ssharm37
"""

from ode import *
import csv
from scipy.optimize import fsolve

def BDF1(func,initial_cond,initial_time,final_time,time_step):
    iterations=int((final_time-initial_time)/time_step)
    y=initial_cond
    t=initial_time
    solution=[y]
    time_stamp=[t]
    
    for i in range (0,iterations):
        def equation(y_1,y):
            return y+time_step*func(y_1)-y_1
        y=fsolve(equation,y+1e-3,epsfcn=1e-4,args=(y,))
        t=t+time_step
        solution.append(y)
        time_stamp.append(t)
        print('Time:',t)
    return solution,time_stamp


def BDF2(func,initial_cond,initial_time,final_time,time_step):
    iterations=int((final_time-initial_time)/time_step)
    y=initial_cond
    t=initial_time
    solution=[y]
    time_stamp=[t]
    y_n1,time=BDF1(foo,initial_cond,initial_time,initial_time+time_step,time_step)
    y_n1=y_n1[-1]
    time=time[-1]
    solution.append(y_n1)
    time_stamp.append(time)
    t=time
    y=y_n1
    for i in range (0,iterations):
        def equation(y_2,y_1,y):
            return 4.0/3.0*y_1+2.0/3.0*time_step*func(y_2)-y/3.0-y_2
        y=fsolve(equation,y+1e-3,epsfcn=1e-4,args=(solution[-1],solution[-2]))
        t=t+time_step
        solution.append(y)
        time_stamp.append(t)
        print('Time:',t)
    return solution,time_stamp

initial_cond=np.array([1.0,0.0,0.0])
initial_time=0.0
final_time=20.0
time_step=1e-3
solution,time_stamp=BDF1(foo,initial_cond,initial_time,final_time,time_step)
    
np.savetxt('Solution_BDF1.csv',solution,delimiter=',')
np.savetxt('Time_stamp_BDF1.csv',time_stamp)

solution,time_stamp=BDF2(foo,initial_cond,initial_time,final_time,time_step)

np.savetxt('Solution_BDF2.csv',solution,delimiter=',')
np.savetxt('Time_stamp_BDF2.csv',time_stamp)

