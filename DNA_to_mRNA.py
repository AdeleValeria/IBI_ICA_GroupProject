# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:14:46 2019

@author: Group2

DNA to mRNA convertor
Write a function that computes the mRNA sequence form any user-specified DNA sequence.
"""

s = input("DNA sequence: ")
c=""

for i in s:
    if i == 'A':
        c=c+'U'
    elif i=='G':
        c=c+'C'
    elif i=='T':
        c=c+'A'
    elif i=='C':
        c=c+'G'
print(c)