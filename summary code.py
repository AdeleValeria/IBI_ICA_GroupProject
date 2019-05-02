#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:35:36 2019

@author: Group 2
"""
import re
# examine the validity of DNA sequence

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
def again():
    task = input('Please select the task you want to do:\n 1. GC content claculator\n 2. Complementary DNA strand calculator\n 3. DNA to mRNA convertor (transcription)\n 4. mRNA to protein (translation)\n 5. effective motif analysis\n 6. quit\n') 
    task()    
task = input('Please select the task you want to do:\n 1. GC content claculator\n 2. Complementary DNA strand calculator\n 3. DNA to mRNA convertor (transcription)\n 4. mRNA to protein (translation)\n 5. effective motif analysis\n')     
def task():    
#---------------------------------task1----------------------------------------
    if task == '1':            
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
        again()
    #---------------------------------task2----------------------------------------
    elif task == '2':
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
         again()
    #---------------------------------task3----------------------------------------
    elif task == '3':
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
            again()
    #---------------------------------task4----------------------------------------
    elif task == '4':
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
        again()
    #---------------------------------task5----------------------------------------  
    elif task == '5':
        from collections import Counter
        filename=input('Input the file path of your sequence:')
        reference=input('Input the reference sequence:')
        n=int(input('Input the length of the start primer:'))
        m=int(input('Input the length of the end primer:'))
        t=int(input('Input the length of the tag:'))
        target=int(input('Input the length of target sequence:'))
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
        print(newnewlist)
        abc=[]
        for i in range(0,len(reference)-target+1):
            for j in newnewlist:
                if j==reference[i:i+target]:
                    abc.append(j)
        counter=Counter(abc)
        L=tuple(counter.keys())
        T=tuple(counter.values())
        for z in range(0,len(L)):
            print(L[z],counter[L[z]]/len(abc)*100 , "%")
        import numpy as np
        import matplotlib.pyplot as plt
        con = np.arange(len(L))
        means = (T)
        width = 0.8
        plt.bar(con,means,width, color = 'lightgrey')
        plt.xticks(con,(L))
        plt.ylabel('amount')
        plt.title('Affinity of different DNA domains')
        plt.show()
        again()
    elif task == '6':
        print('THank you for using!')
         quit
    else:
        task = input('Please input a valid number:\n 1. GC content claculator\n 2. Complementary DNA strand calculator\n 3. DNA to mRNA convertor (transcription)\n 4. mRNA to protein (translation)\n 5. effective motif analysis\n') 
        task()          