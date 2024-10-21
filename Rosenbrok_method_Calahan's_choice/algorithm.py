# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:18:38 2024

@author: ssharm37
"""

from ode import *
import csv
from scipy.optimize import approx_fprime
from scipy.integrate import solve_ivp

def Rosenbrock(func,initial_cond,initial_time,final_time,time_step):
    iterations=int((final_time-initial_time)/time_step)
    y=initial_cond
    t=initial_time
    solution=[y]
    time_stamp=[t]
    for i in range (0,iterations):
        jacobian=approx_fprime(y,func,1e-4)
        I=np.identity(len(y))
        a1=0.5*(1.0+1.0/3.0**0.5)
        a21=-2.0/3.0**0.5
        w1=0.75
        w2=0.25
        b1=np.linalg.inv(I-a1*time_step*jacobian)*time_step@func(y)
        b2=np.linalg.inv(I-a1*time_step*jacobian)*time_step@func(y+a21*b1)
        y=y+w1*b1+w2*b2
        t=t+time_step
        solution.append(y)
        time_stamp.append(t)
        print('Time:',t)
    return solution,time_stamp

initial_cond=np.array([1.0,0.0,0.0])
initial_time=0.0
final_time=200.0
time_step=1e-3
solution,time_stamp=Rosenbrock(foo,initial_cond,initial_time,final_time,time_step)
    

# def wrapper(t,y):
#     return foo(y)

# solution=solve_ivp(wrapper,[initial_time,final_time], initial_cond,method='LSODA')
# time_stamp=solution.t
# solution1=solution.y
# import matplotlib.pyplot as plt

# plt.plot(time_stamp,solution.y[2,:])
# plt.show()

np.savetxt('Solution.csv',solution,delimiter=',')
np.savetxt('Time_stamp.csv',time_stamp)