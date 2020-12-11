# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:24:45 2019

@author: andok
"""
import numpy as np
def extractNames(fileName) :
    file = open(fileName,"r") 
    lines = file.readlines()
    
    file.close()
    for i in range(len(lines)) :
        lines[i] = lines[i].lower()
    return lines

basic_dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8,
        "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15,
        "p" : 16,"q" :17 , "r" : 18,"s" : 19,"t" : 20,"u" : 21,"v" : 22, "w" : 23, "x" : 24, 
        "y" : 25, "z" : 26, "é" : 27, "è" : 28, "\n" : 0,}


basic_alphabet = ["\n", "a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", 
            "n", "o", "p" ,"q" , "r","s","t","u","v", "w", "x", "y", "z", "é", "è" ]

smart_dict = {"\n" : 0,"a" : 1, "o" : 2, "u" : 3, "e" : 4, "è" : 5, "é" : 6, "i" : 7, "y" : 8,
        "w" : 9, "v" : 10, "f" : 11, "h" : 12, "c" : 13, "s" : 14, "z" : 15,
        "j" : 16,"g" :17 , "r" : 18,"t" : 19,"k" : 20,"x" : 21,"q" : 22, "d" : 23, "p" : 24, 
        "b" : 25, "l" : 26, "m" : 27, "n" : 28, }


smart_alphabet = list(smart_dict.keys())

voy = {"a" : True, "b" : False, "c" : False, "d" : False, "e" : True, "f" : False, "g" : False, "h" : False,
        "i" : True, "j" : False, "k" : False, "l" : False, "m" : False, "n" : False, "o" : True,
        "p" : False,"q" :False, "r" : False,"s" : False,"t" : False,"u" : True,"v" : False, "w" : False, "x" : False, 
        "y" : False, "z" : False, "é" : True, "è" : True, "\n" : False,}

alphabet = smart_alphabet
dict = smart_dict

Nalph = len(alphabet)

def computeFreq(names) :
    freq = np.zeros(Nalph)
    tot = 0
    for n in names :
        for letter in n :
            freq[dict[letter]] += 1
            if dict[letter]!=0:
                tot+=1
    return freq[1:]/tot

def computeFirstLetterFreq(names) :
    freq = np.zeros(Nalph)

    for n in names :
        freq[dict[n[0]]] += 1
    return freq[1:]/float(len(names))

def computeTransMat(names) :
    mat = np.zeros((Nalph, Nalph))
    for nm in names : 
        for i in range(len(nm) - 1) :
            first = dict[nm[i]]
            next = dict[nm[i+1]]
            mat[first][next] += 1
    for k in range(Nalph) :
        s = sum(mat[k])
        if s > 0 :
            mat[k] = mat[k]/s      
    return mat
            
def nextStep(seq, prob) :
    nxt = np.random.choice(range(Nalph), p = prob)
    
    if len(seq)<4 and nxt==0 : 
        k = 4
        while nxt==0 and k>0 :      
            nxt = np.random.choice(range(Nalph), p = prob)
            k-=1
            
        nxt = np.random.choice(range(Nalph), p = prob)
    
    if len(seq)>7 and nxt!=0 :
        k = 0
        while nxt!=0 and k<len(seq) :      
            nxt = np.random.choice(range(Nalph), p = prob)
            k+=1
        
    if len(seq)>2  :
        minus1letter = alphabet[seq[-1]]
        minus2letter = alphabet[seq[-2]]
        
        if not (voy[minus2letter] or voy[minus1letter]):
            letter = alphabet[nxt]
            k=0
            while (not voy[letter]) and k<4 :  
                nxt = np.random.choice(range(Nalph), p = prob)
                letter = alphabet[nxt]
                k+=1 
        if  (voy[minus2letter] and voy[minus1letter]):
            letter = alphabet[nxt]
            k=0
            while (voy[letter]) and k<6 :  
                nxt = np.random.choice(range(Nalph), p = prob)
                letter = alphabet[nxt]
                k+=1 
    
    return nxt

def nameToVect(name) :
    
    name = name.lower()
    vect = np.zeros(33)
    i = 0
    for letter in name :
        vect[i] = dict[letter]
        i+=1
    i = 16
    for letter in name :
        vect[i] = int(voy[letter])
        i+=1
    vect[32] = len(name)
    return vect

def vectToName(vect) :
    num = int(vect[0])
    i = 0
    name = alphabet[num].upper()
    while num !=0 :
        i+=1
        
        num = int(vect[i])
        name+= alphabet[num] 
    return name

        
        

def generateName(mat, flfreq):
    cur = int(np.random.choice(range(1, Nalph), p = flfreq))
    seq = [cur]
    step_cpt = 0
    while ((step_cpt<14) and (cur>0)) :
        nxt = nextStep(seq, mat[cur])
        seq.append(nxt)
        cur = nxt
        step_cpt += 1
        
    if step_cpt==14 :
        seq.append(0)
        
    
    name = str(alphabet[seq[0]]).upper()
    
    for i in seq[1:] :
        name += alphabet[i]
    return name, seq
    
