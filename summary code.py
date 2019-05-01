#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:35:36 2019

@author: chenghui
"""
import re

def detect_DNA(DNA):
    if re.match(r'[ATGC]+$',DNA):
           quit
    else:
            DNA = input('It is an invalid DNA sequence, please input again:')
            detect_DNA(DNA)
#---------------------------------task1----------------------------------------
            
DNA=input("Please input the DNA sequence:\n")
detect_DNA(DNA)
Sequence=list(DNA)
#count 
A=0
T=0
C=0
G=0
for i in Sequence:
    if i == "A":
        A=A+1
        #a+=1
    elif i == "T":
        T=T+1
    elif i == "C":
        C=C+1
    elif i == "G":
        G=G+1
P = (G+C)/(len(Sequence))*100
print("The proportion of Guanine-Cytosine base pairs in the DNA sequence is", int(P), "%")
#---------------------------------task2----------------------------------------
DNA=input("Please input the DNA sequence (5’ to 3’):\n")
detect_DNA(DNA)
Complementary=""
for i in DNA:
    if i == 'A':
       Complementary += 'T'
    elif i=='T':
         Complementary += 'A'
    elif i=='G':
         Complementary += 'C'
    elif i=='C':
         Complementary += 'G'
Complementary_sequence=Complementary[::-1]
print('The complementary DNA sequence (5’ to 3’):', Complementary_sequence)

#---------------------------------task3----------------------------------------

def Translation(seq):
    DNA=input("Please input the DNA sequence (5’ to 3’):\n")
    mRNA=""
    for i in DNA:
        if i == 'A':
            mRNA += 'U'
        elif i=='T':
            mRNA +='A'
        elif i=='G':
            mRNA +='C'
        elif i=='C':
            mRNA +='G'
    print('The mRNA sequence is:', mRNA)

