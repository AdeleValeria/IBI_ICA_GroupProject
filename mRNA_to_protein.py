# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:15:53 2019

@author: Group2

mRNA to protein
Write a function that computes a polypeptide sequence from any user-specified mRNA sequence.
For simplicity, you are allowed to assume that the mRNA contains exactly one start codon and one
stop codon. 
"""
'''
Written by Alana
'''
#------------------------------------------------------------------------------
import re
S=''
mRNA = input('input the mRNA sequence:')
if re.match(r'[^AUGC]+$',mRNA):
   mRNA = input('It is an invalid mRNA sequence,please input again:')
AA = {'U':{'U':{'U':'F','C':'F','A':'L','G':'L'},'C':{'U':'S','C':'S','A':'S','G':'S'},'A':{'U':'Y','C':'Y','A':'','G':''},'G':{'U':'C','C':'C','A':'','G':'W'}},
      'C':{'U':{'U':'L','C':'L','A':'L','G':'L'},'C':{'U':'P','C':'P','A':'P','G':'P'},'A':{'U':'H','C':'H','A':'Q','G':'Q'},'G':{'U':'R','C':'R','A':'R','G':'R'}},
      'A':{'U':{'U':'I','C':'I','A':'M','G':'M'},'C':{'U':'T','C':'T','A':'T','G':'T'},'A':{'U':'N','C':'N','A':'K','G':'K'},'G':{'U':'S','C':'S','A':'R','G':'R'}},
      'G':{'U':{'U':'V','C':'V','A':'V','G':'V'},'C':{'U':'A','C':'A','A':'A','G':'A'},'A':{'U':'D','C':'D','A':'E','G':'E'},'G':{'U':'G','C':'G','A':'G','G':'G'}}}
if re.search('AUG',mRNA):
   m= mRNA.index('AUG')
for i in range (m,len(mRNA),3):
    P=AA[mRNA[i]][mRNA[i+1]][mRNA[i+2]]
    if P == '':
       break
    else: 
        S += P
print(S)
#------------------------------------------------------------------------------