# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:12:48 2019

@author: sissy
"""

from collections import Counter
filename=input('Input the file path of your data:')
n=int(input('Input the length of the start primer:'))
m=int(input('Input the length of the end primer:'))
t=int(input('Input the length of the tag:'))
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
print(newlist)
newnewlist=[]
for j in range(0, len(newlist)):
    s=newlist[j][n:len(newlist[j])-m-t]
    newnewlist.append(s)
dict={}
for key in newnewlist:
    if key in dict.keys():
        dict[key]+=1
    else:
        dict[key]=1
print(dict)
LL=tuple(dict.keys())
print(LL[1])

#for key,value in dict.items():
#    print(key)
#LL=dict.item()
#print(LL)
counter=Counter(newnewlist)
print(counter)