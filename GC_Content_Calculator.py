# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:58:24 2019

@author:Group2

GC Content Calculator
GC content, i.e. the fraction of total DNA that is comprised of Guanine and Cytosine nucelotides,
varies from species to species. Guanine-Cytosine base pairs use three hydrogen bonds, whereas
Adenine-Thymine base pairs use only two. This means that the stability of the DNA double helix
and consequently its “melting temperature”, i.e. the temperature that is required to separate both
strands in the lab, varies depending on GC content. It is therefore useful to be able to compute the
GC content.

Write a function that computes the GC content (in % of total bases) for any user-specified DNA
sequence. 
"""


B=input("give me a sequence of DNA:\n")
S=list(B)
#count 
a=0
t=0
c=0
g=0
for i in S:
    if i == "A":
        a=a+1
        #a+=1
    elif i == "T":
        t=t+1
    elif i == "C":
        c=c+1
    elif i == "G":
        g=g+1
    else:
        print("The sequence is wrong.")
#print
z = (g+c)/(len(S))*100
print("The proportion of G and C in the DNA sequence is", int(z), "%")