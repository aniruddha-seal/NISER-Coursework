#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:57:21 2020

@author: acer
"""

import numpy as np
import math
import matplotlib.pyplot as plt

k_B=1.38*(10**(-23))
T=np.arange(0.1,300000.0,200.0)
print(len(T))
u=np.zeros(len(T))
s=np.zeros(len(T))
Q=np.zeros(len(T))
cv=np.zeros(len(T))
e=5*1.602*(10**(-19))

for i in range(len(T)):
    u[i]=e*(math.exp(-e/(k_B*T[i]))+2*math.exp(-2*e/(k_B*T[i])))/(1+math.exp(-e/(k_B*T[i]))+math.exp(-2*e/(k_B*T[i])))
    s[i]=k_B*math.log(1+math.exp(-e/(k_B*T[i]))+math.exp(-2*e/(k_B*T[i])))+(u[i]/T[i])
    Q[i]=1+math.exp(-e/(k_B*T[i]))+math.exp(-2*e/(k_B*T[i]))
    cv[i]=(e**2/(k_B*(T[i]**2)))*(((math.exp(-e/(k_B*T[i]))+4*math.exp(-2*e/(k_B*T[i])))/Q[i])-((math.exp(-e/(k_B*T[i]))+4*math.exp(-2*e/(k_B*T[i])))/Q[i])**2)
    print(s[i])

fig=plt.figure(dpi=650)
#plt.ylim(0.0,(8.0*(10**(-19))))
plt.plot(T,cv)
plt.xlabel("T (in K)")
plt.ylabel("Specific Heat(T) (in J/K)")
plt.tight_layout()
plt.savefig("1e.png",format="png")
#plt.legend()
plt.show()
                                                          