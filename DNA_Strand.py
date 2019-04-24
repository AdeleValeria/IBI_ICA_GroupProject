# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:12:59 2019

@author: Group2

Complementary DNA strand calculator
Write a function that computes the complementary DNA strand (from 5’ to 3’) for any userspecified
DNA sequence (assuming the user has also specified it 5’ to 3’)
"""

s = input("DNA sequence: ")
re=s[::-1]
c=""

for i in re:
    if i == 'A':
        c=c+'T'
    elif i=='G':
        c=c+'C'
    elif i=='T':
        c=c+'A'
    elif i=='C':
        c=c+'G'
print(c)