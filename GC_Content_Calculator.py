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


DNA=input("Please input the DNA sequence:\n")

S=list(B)
#count 
A=0, T=0, C=0,G=0
for i in S:
    if i == "A":
        A=A+1
        #a+=1
    elif i == "T":
        T=T+1
    elif i == "C":
        C=C+1
    elif i == "G":
        G=G+1

#print
z = (g+c)/(len(S))*100
print("The proportion of G and C in the DNA sequence is", int(z), "%")