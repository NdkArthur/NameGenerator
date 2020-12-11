# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:09:43 2019

@author: andok
"""

import generator

print("\n## Name generator")
      
filename = input("Choose names' file : ")
      
while(True) :  
    names = extractNames(filename)
    flfreq = computeFirstLetterFreq(names)  
    mat =  computeTransMat(names)
    name, _ =  generateName(mat, flfreq)
    print("\nGenerated name : " + name)
    print(vectToName(nameToVect(name)))
    ans = input(" -> another [y/n] ? ")
    if ans!="y" :
        break
print("Name generator exited")    


    