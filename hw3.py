# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7hyirMN30qW8U6Tj4b4b4PeIcBBQUuO
"""

from numpy import *
S=160
u=1.5
d=0.5
R=1.2
N=3
X=150
p=(R-d)/(u-d)
S_n=[S]
P_n=[1]
ud=array([u,d])
pq=array([p,1-p])
for n in range(1,N+1):
  sn=array(S_n[n-1])
  sn.transpose()
  pn=array(P_n[n-1])
  pn.transpose()
  if n==1 :
    Sn=dot(sn,ud)
    Pn=dot(pn,pq)
  else:
    Sn=outer(sn,ud)
    Pn=outer(pn,pq)
  S_n.append(Sn.flatten('F'))
  P_n.append(Pn.flatten('F'))
C,P=0,0
for i in range(len(P_n[n])) :
  C+=P_n[n][i]*max(0,S_n[n][i]-X)
  P+=P_n[n][i]*max(0,X-S_n[n][i])
print('call/put')
print(str(round(C/R**n,3))+'/'+str(round(P/R**n,3)))