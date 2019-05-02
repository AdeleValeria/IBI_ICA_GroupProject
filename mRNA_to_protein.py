# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:15:53 2019

@author: Group2

mRNA to protein
Write a function that computes a polypeptide sequence from any user-specified mRNA sequence.
For simplicity, you are allowed to assume that the mRNA contains exactly one start codon and one
stop codon. 
"""

#------------------------------------------------------------------------------
import re
def detect(mRNA):
    if re.match(r'[AUGC]+$',mRNA):
       quit
    else:
        mRNA = input('It is an invalid mRNA sequence,please input again:')
        detect(mRNA)
        
def start (mRNA):
    global start_index
    if re.search('AUG',mRNA):
       start_index = mRNA.index('AUG')
    else:
        mRNA = input('Please input the correct mRNA sequence with a start codon:')
        start(mRNA)  
        
def stop (mRNA):
    mRNA = input('Please input the correct mRNA sequence with a stop codon:')
    mRNA_protein()    
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
    detect (mRNA)
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