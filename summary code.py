#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:35:36 2019

@author: Group 2
"""
import re
# examine the validity of DNA sequence
task = input('Please select the task you want to do:\n 1. GC content claculator\n 2. Complementary DNA strand calculator\n 3. DNA to mRNA convertor (transcription)\n 4. mRNA to protein (translation)\n') 
def detect_DNA(DNA):
    if re.match(r'[ATGC]+$',DNA):
           quit
    else:
            DNA = input('It is an invalid DNA sequence, please input again:')
            detect_DNA(DNA)
            
# examine the validity of mRNA sequence
def detect_mRNA(mRNA):
    if re.match(r'[AUGC]+$',mRNA):
       quit
    else:
        mRNA = input('It is an invalid mRNA sequence,please input again:')
        detect_mRNA(mRNA)       
        
# examine if the mRNA sequence includes a start codon          
def start (mRNA):
    global start_index
    if re.search('AUG',mRNA):
       start_index = mRNA.index('AUG')
    else:
        mRNA = input('Please input the correct mRNA sequence with a start codon:')
        start(mRNA)  
        
# examine if the mRNA sequence includes a stop codon         
def stop (mRNA):
    mRNA = input('Please input the correct mRNA sequence with a stop codon:')
    mRNA_protein()    
#---------------------------------task1----------------------------------------
            
DNA=input("Please input the DNA sequence:\n")
detect_DNA(DNA)
A=0
T=0
C=0
G=0
for i in DNA:
    if i == "A":
        A += 1
    elif i == "T":
        T += 1
    elif i == "C":
        C += 1
    elif i == "G":
        G += 1
P = (G+C)/(len(DNA))*100
print("The proportion of Guanine-Cytosine base pairs in the DNA sequence is", P, "%")

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
    detect_DNA(DNA)
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

#---------------------------------task4----------------------------------------
mRNA = ''
start_index = 0
amino_acid=''
sequence=''  
AA = {'U':{'U':{'U':'F','C':'F','A':'L','G':'L'},
           'C':{'U':'S','C':'S','A':'S','G':'S'},
           'A':{'U':'Y','C':'Y','A':' ','G':' '},
           'G':{'U':'C','C':'C','A':' ','G':'W'}},
      'C':{'U':{'U':'L','C':'L','A':'L','G':'L'},
           'C':{'U':'P','C':'P','A':'P','G':'P'},
           'A':{'U':'H','C':'H','A':'Q','G':'Q'},
           'G':{'U':'R','C':'R','A':'R','G':'R'}},
      'A':{'U':{'U':'I','C':'I','A':'I','G':'M'},
           'C':{'U':'T','C':'T','A':'T','G':'T'},
           'A':{'U':'N','C':'N','A':'K','G':'K'},
           'G':{'U':'S','C':'S','A':'R','G':'R'}},
      'G':{'U':{'U':'V','C':'V','A':'V','G':'V'},
           'C':{'U':'A','C':'A','A':'A','G':'A'},
           'A':{'U':'D','C':'D','A':'E','G':'E'},
           'G':{'U':'G','C':'G','A':'G','G':'G'}}} 
def mRNA_protein ():
    global sequence
    detect_mRNA (mRNA)
    start (mRNA)
    for i in range (start_index,len(mRNA),3):
        if i <= len(mRNA)-3:
           amino_acid = AA[mRNA[i]][mRNA[i+1]][mRNA[i+2]]
           if amino_acid != ' ' and i<len(mRNA)-3:
              sequence += amino_acid
           elif amino_acid !=' ' and i == len(mRNA)-3:
                stop(mRNA)
           else:
               break
        else:
            stop(mRNA)
    print('The protein sequence is:',sequence)   

mRNA = input('input the mRNA sequence:')
mRNA_protein()     

#---------------------------------task5----------------------------------------            