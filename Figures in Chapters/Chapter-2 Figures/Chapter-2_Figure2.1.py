# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

cn1=lambda a: a*(a-1)

cn2=lambda a: a*(a-1)*(a-2)

cn3=lambda a: a*(a-1)*(a-2)*(a-3)

cn4=lambda a: a*(a-1)*(a-2)*(a-3)*(a-4)

cn12=lambda a: a*(a-1)*(a-2)*(a-3)*(a-4)*(a-5)*(a-6)*(a-7)*(a-8)*(a-9)*(a-10)*(a-11)*(a-12)

x=np.linspace(0,4,4000)
#%%
plt.figure(1,dpi=600)
plt.plot(x,abs(cn1(x)),color='black')
plt.scatter(0.5,0.25,color='red',marker=10,s=70)
plt.xlim([0,1])
plt.ylim([0,0.3])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.text(0.25, 0.15, r'Max error at $\alpha =0.5$', fontsize = 16)
plt.savefig('Figure2.1_order1.png')
plt.show()
#%%
plt.figure(2,dpi=600)
plt.plot(x,(cn2(x)),color='black')
plt.scatter(0.42,2/(3*np.sqrt(3)),color='red',marker=10,s=70)
plt.scatter(1.58,-2/(3*np.sqrt(3)),color='red',marker=10,s=70)
plt.xlim([0,2])
plt.ylim([-0.5,0.5])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.text(0.7, 0.3, r'Max error at $\alpha =0.42, 1.58$', fontsize = 16)
plt.savefig('Figure2.1_order2.png')
plt.show()
#%%
plt.figure(3,dpi=600)
plt.plot(x,(cn3(x)),color='black')
plt.scatter(0.382,-1,color='red',marker=10,s=70)
plt.scatter(2.618,-1,color='red',marker=10,s=70)
plt.scatter(1.5,0.5625,color='red',marker=10,s=70)
plt.xlim([0,3])
plt.ylim([-1.2,0.75])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.text(0.4, 0.62, r'Max error at $\alpha =0.382, 2.618, 1.5$', fontsize = 16)
plt.savefig('Figure2.1_order3.png', bbox_inches='tight')
plt.show()
#%%
plt.figure(4,dpi=600)
plt.plot(x,(cn4(x)),color='black')
plt.scatter(0.35,cn4(0.35),color='red',marker=10,s=70)
plt.scatter(4-0.35,cn4(4-0.35),color='red',marker=10,s=70)
# plt.scatter(1.5,0.5625,color='red',marker=10,s=70)
plt.xlim([0,4])
plt.ylim([-4,4])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.text(1, 2, r'Max error is near boundary', fontsize = 16)
plt.savefig('Figure2.1_order4.png')
plt.show()
#%%
y=np.linspace(0,12,12000)
plt.figure(5,dpi=600)
plt.plot(y,(cn12(y)),color='black')
# plt.scatter(0.35,cn4(0.35),color='red',marker=10,s=70)
# plt.scatter(4-0.35,cn4(4-0.35),color='red',marker=10,s=70)
# plt.scatter(1.5,0.5625,color='red',marker=10,s=70)
plt.xlim([0,12])
# plt.ylim([-4,4])
plt.grid()
plt.xlabel(r'$\alpha$',fontsize=16)
plt.ylabel('Value',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.text(1, 2, r'Max error is near boundary', fontsize = 16)
plt.savefig('Figure2.1_order12.png')
plt.show()