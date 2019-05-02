# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:12:48 2019

@author: sissy
"""

from collections import Counter
filename=input('Input the file path of your sequence:')
reference=input('Input the reference sequence:')
n=int(input('Input the length of the start primer:'))
m=int(input('Input the length of the end primer:'))
t=int(input('Input the length of the tag:'))
target=int(input('Input the length of target sequence:'))
data=open(filename)
list=[]
for line in data.readlines():
    temp1=line.strip('\n')
    list.append(temp1)
data.close()
newlist=[]
newlist.append(list[1])
for i in range(1,len(list)):
    if list[i] not in newlist:
        newlist.append(list[i])
newnewlist=[]
for j in range(0, len(newlist)):
    s=newlist[j][n:len(newlist[j])-m-t]
    newnewlist.append(s)
abc=[]
for i in range(0,len(reference)-target+1):
    for j in newnewlist:
        if j==reference[i:i+target]:
            abc.append(j)
counter=Counter(abc)
L=tuple(counter.keys())
T=tuple(counter.values())
for z in range(0,len(L)):
    print(L[z],counter[L[z]]/len(abc)*100 , "%")
import numpy as np
import matplotlib.pyplot as plt
con = np.arange(len(L))
means = (T)
width = 0.8
plt.bar(con,means,width, color = 'lightgrey')
plt.xticks(con,(L))
plt.ylabel('amount')
plt.title('Affinity of different DNA domains')
plt.show()