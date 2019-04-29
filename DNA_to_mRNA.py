# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:14:46 2019

@author: Group2

DNA to mRNA convertor
Write a function that computes the mRNA sequence form any user-specified DNA sequence.
"""
import re
def DNAtomRNA(seq):
    s=""
    for i in seq:
        if i == 'A':
            s=s+'U'
        elif i=='G':
            s=s+'C'
        elif i=='T':
            s=s+'A'
        elif i=='C':
            s=s+'G'
    print(s)


input_seq = input("DNA sequence: ")
if re.match(r"^[ATGC]+$", input_seq):
    DNAtomRNA(input_seq)
else:
    print("invalid DNA sequence")