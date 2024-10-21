# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:09:55 2024

@author: ssharm37
"""

import numpy as np
from parameters import k1,k2,k3 #imports all parameter values from the file:'parameters'

def foo(t,y):
    F=np.zeros(len(y))
    y1,y2,y3=y
    F=-k1*y1+k2*y2*y3, k1*y1-k2*y2*y3-k3*y2**2.0, k3*y2**2.0
    return np.array(F)
    


