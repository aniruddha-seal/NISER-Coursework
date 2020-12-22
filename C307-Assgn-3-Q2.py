#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:11:34 2020

@author: acer
"""
import numpy as np
import math
import matplotlib.pyplot as plt

eV=1.6*(10**(-19))
e1=0.025*eV
e2=1.2*eV
k_B=1.38*(10**(-23))
T=np.arange(0.1,80000.0,200.0)
p1=np.zeros(len(T))
p2=np.zeros(len(T))
p3=np.zeros(len(T))
q=np.zeros(len(T))
e=np.zeros(len(T))
for i in range(len(T)):
    q[i]=1+math.exp(-e1/(k_B*T[i]))+math.exp(-e2/(k_B*T[i]))
    p1[i]=1/q[i]
    p2[i]=math.exp(-e1/(k_B*T[i]))/q[i]
    p3[i]=math.exp(-e2/(k_B*T[i]))/q[i]
    e[i]=(e1*math.exp(-e1/(k_B*T[i]))+e2*math.exp(-e2/(k_B*T[i])))/q[i]

fig=plt.figure(dpi=650)
#plt.plot(T,p1,label="P(E=0 eV)")
#plt.plot(T,p2,label="P(E=0.025 eV)")
#plt.plot(T,p3,label="P(E=1.2 eV)")
plt.plot(T,e)
plt.xlabel("T (in K)")
plt.ylabel("<E> (in J)")
#plt.ylabel("P(E)")
#plt.legend()
plt.tight_layout()
plt.savefig("2e.png",format="png")
plt.show()